#!/usr/bin/env bash
###############################################################################
#  פרסום מחקר "רחל צדוק" ל-GitHub + GitHub Pages
#
#  איך מריצים (פעם אחת), בטרמינל על ה-Mac:
#     cd ~/Library/CloudStorage/Dropbox/"רחל צדוק"
#     bash publish_to_github.sh
#
#  דרישות: git + GitHub CLI (gh).  אם gh לא מותקן:  brew install gh
#  בפעם הראשונה gh יבקש להתחבר לחשבון GitHub שלך (דרך הדפדפן) — זה תקין.
###############################################################################
set -euo pipefail

REPO_NAME="rachel-zadok-research"    # שם הריפו
VISIBILITY="public"                  # public = נדרש לאתר Pages חינמי

cd "$(dirname "$0")"
echo "📂 עובד בתיקייה: $(pwd)"

# ── 1. קובצי תשתית (נוצרים רק אם חסרים) ──────────────────────────────────────
if [ ! -f .gitignore ]; then
cat > .gitignore <<'EOF'
# קבצי אודיו כבדים (חורגים ממגבלת 100MB של GitHub)
*.mp3
*.wav
*.m4a
/testimony.mp3
/testimony_16k.wav
transcript_raw.txt
# עבודה / זמניים
chunks/
ארכיון_עבודה/
site/
__pycache__/
*.pyc
.DS_Store
EOF
echo "✓ נוצר .gitignore"
fi

# .nojekyll — מונע מ-GitHub Pages לסנן קבצים/תיקיות
touch .nojekyll

if [ ! -f README.md ]; then
cat > README.md <<'EOF'
# מחקר גנאלוגי — רחל צדוק (לבית סטרולוביץ-רפפורט)

מחקר תיעודי על רחל ("רוצי") צדוק, ילידת 16.04.1929 בוולובה / Ökörmező / מיז'יריה,
ניצולת אושוויץ, שטוטהוף וטורן. שבעה דורות, מסלול הרדיפה בשואה, וגורל בני המשפחה —
מבוסס על מסמכים ומקורות ראשוניים.

**האתר החי:** [רחל_צדוק_המחקר_המלא.html](רחל_צדוק_המחקר_המלא.html)
(דף הכניסה index.html מפנה אליו אוטומטית.)
EOF
echo "✓ נוצר README.md"
fi

# ── 2. git ───────────────────────────────────────────────────────────────────
if [ ! -d .git ]; then
  git init -q
  git branch -M main
fi
git add -A
git commit -q -m "מחקר רחל צדוק — דוח מלא, ראיות, עצי משפחה ואינדקס מקורות" || echo "ℹ️  אין שינויים חדשים לשמירה"

# ── 3. ודא ש-gh מחובר ────────────────────────────────────────────────────────
if ! command -v gh >/dev/null 2>&1; then
  echo "❌ GitHub CLI (gh) לא מותקן. התקן עם:  brew install gh   ואז הרץ שוב."
  exit 1
fi
if ! gh auth status >/dev/null 2>&1; then
  echo "🔑 מתחבר ל-GitHub (ייפתח דפדפן / קוד חד-פעמי)…"
  gh auth login --hostname github.com --git-protocol https --web --scopes repo
fi

OWNER=$(gh api user --jq .login)
echo "👤 חשבון: $OWNER"

# ── 4. צור את הריפו (אם לא קיים) ודחוף ───────────────────────────────────────
if gh repo view "$OWNER/$REPO_NAME" >/dev/null 2>&1; then
  echo "ℹ️  הריפו $OWNER/$REPO_NAME כבר קיים — דוחף עדכון."
  git remote get-url origin >/dev/null 2>&1 || git remote add origin "https://github.com/$OWNER/$REPO_NAME.git"
  git push -u origin main
else
  gh repo create "$REPO_NAME" --"$VISIBILITY" --source=. --remote=origin --push \
     --description "מחקר גנאלוגי תיעודי על רחל צדוק (סטרולוביץ-רפפורט), ניצולת השואה מוולובה"
fi

# ── 5. הפעל GitHub Pages (מהשורש של main) ────────────────────────────────────
echo "🌐 מפעיל GitHub Pages…"
gh api -X POST "repos/$OWNER/$REPO_NAME/pages" \
   -f "source[branch]=main" -f "source[path]=/" >/dev/null 2>&1 \
   || gh api -X PUT "repos/$OWNER/$REPO_NAME/pages" \
        -f "source[branch]=main" -f "source[path]=/" >/dev/null 2>&1 \
   || echo "ℹ️  אם Pages לא הופעל אוטומטית — הפעל ידנית ב-Settings → Pages (Branch: main, Folder: / root)."

echo ""
echo "✅ הושלם!"
echo "   ריפו:  https://github.com/$OWNER/$REPO_NAME"
echo "   אתר:   https://$OWNER.github.io/$REPO_NAME/"
echo "   (ל-Pages לוקח 1–2 דקות לעלות בפעם הראשונה.)"
