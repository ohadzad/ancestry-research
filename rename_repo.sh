#!/usr/bin/env bash
# ---------------------------------------------------------------------------
#  שינוי שם הריפו:  zadok-ancestry-research  ->  ancestry-research
#  מעדכן גם את כל האזכורים בטקסט, את ה-venv, ודוחף.
#
#  הרצה:  cd אל תיקיית הריפו, ואז   bash rename_repo.sh
#  DRY_RUN=1 כדי לראות מה ישתנה בלי לשנות שם, לקמט או לדחוף.
# ---------------------------------------------------------------------------
set -euo pipefail

OLD="zadok-ancestry-research"
NEW="ancestry-research"

cd "${1:-$PWD}"
git rev-parse --git-dir >/dev/null 2>&1 || { echo "✗ $PWD אינו ריפו git"; exit 1; }
command -v gh >/dev/null || { echo "✗ חסר: gh"; exit 1; }

OWNER="$(gh api user --jq .login)"
CUR="$(basename -s .git "$(git remote get-url origin)")"
echo "▸ ריפו נוכחי: $OWNER/$CUR"

if [ -n "$(git status --porcelain | grep -v 'restructure_to_portal.sh\|rename_repo.sh' || true)" ]; then
  echo "✗ יש שינויים לא מקומיטים. קמט או נקה אותם קודם:"
  git status --short | head -10
  exit 1
fi

# --- 1. אזכורי טקסט בקבצים מנוהלים (בלי docs/ ובלי בינאריים) ---------------
echo "▸ מחליף אזכורים של $OLD ..."
FILES="$(git grep -l -- "$OLD" -- . ':!*docs/*' ':!*site/*' || true)"
if [ -z "$FILES" ]; then
  echo "  · אין אזכורים בקבצים מנוהלים"
else
  printf '%s\n' "$FILES" | while IFS= read -r f; do
    echo "    $f"
    [ "${DRY_RUN:-0}" = "1" ] || perl -pi -e "s/\Q$OLD\E/$NEW/g" "$f"
  done
fi
# הסקריפטים העוזרים אינם מנוהלים — לעדכן גם אותם אם הם כאן
for f in restructure_to_portal.sh rename_repo.sh; do
  if [ -f "$f" ] && grep -q -- "$OLD" "$f"; then
    echo "    $f  (לא מנוהל)"
    [ "${DRY_RUN:-0}" = "1" ] || perl -pi -e "s/\Q$OLD\E/$NEW/g" "$f"
  fi
done

# --- 1b. הסקריפט הזה לא נכנס לריפו ------------------------------------------
if [ -f .gitignore ] && ! grep -qx 'rename_repo.sh' .gitignore; then
  echo "▸ מוסיף rename_repo.sh ל-.gitignore"
  [ "${DRY_RUN:-0}" = "1" ] || printf 'rename_repo.sh\n' >> .gitignore
fi

# --- 2. ה-venv --------------------------------------------------------------
# לא מזיזים venv קיים: הנתיבים המוחלטים צרובים בתוכו. בונים חדש ומוחקים ישן.
OLDV="$HOME/.venvs/$OLD"; NEWV="$HOME/.venvs/$NEW"
if [ "${DRY_RUN:-0}" = "1" ]; then
  echo "▸ (יבשה) venv: $OLDV -> $NEWV"
elif [ ! -x "$NEWV/bin/python" ] && [ -d "$OLDV" ]; then
  echo "▸ בונה venv חדש: $NEWV"
  python3 -m venv "$NEWV"
  "$NEWV/bin/python" -m pip install --quiet --upgrade pip
  "$NEWV/bin/python" -m pip install --quiet markdown pillow
  rm -rf "$OLDV"
  echo "  ✓ הישן נמחק: $OLDV"
fi

if [ "${DRY_RUN:-0}" = "1" ]; then
  echo
  echo "▸ DRY_RUN=1 — לא שיניתי שם, לא קימטתי ולא דחפתי."
  exit 0
fi

# --- 3. שינוי השם ב-GitHub (מעדכן גם את origin) ----------------------------
if [ "$CUR" != "$NEW" ]; then
  echo "▸ משנה שם: $CUR -> $NEW"
  gh repo rename "$NEW" --yes
else
  echo "▸ השם כבר $NEW"
fi

# --- 4. קומיט ודחיפה --------------------------------------------------------
if [ -n "$(git status --porcelain | grep -v 'restructure_to_portal.sh\|rename_repo.sh' || true)" ]; then
  git add -A
  git commit -m "שינוי שם הריפו ל-$NEW ועדכון הכתובות בתיעוד"
  git push
else
  echo "▸ אין שינויי טקסט לקמט"
fi

echo
echo "✓ בוצע."
echo "  האתר:  https://$OWNER.github.io/$NEW/"
echo "  רחל:   https://$OWNER.github.io/$NEW/rachel-zadok/"
echo
echo "⚠ https://$OWNER.github.io/$OLD/ יפסיק לעבוד — Pages לא מפנה אחרי שינוי שם."
echo "  תן ל-Pages דקה־שתיים לבנות."
