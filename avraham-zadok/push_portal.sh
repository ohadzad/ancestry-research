#!/bin/bash
# ===== אבחון ודחיפה של הפורטל =====
# הרצה: bash "<תיקיית המחקר>/push_portal.sh"
PORTAL="$HOME/Library/CloudStorage/Dropbox/רחל צדוק"
cd "$PORTAL" || exit 1

echo "===== 1. איפה אנחנו ====="
git rev-parse --abbrev-ref HEAD
git remote -v

echo ""
echo "===== 2. מה לא מחויב ====="
git status --short | head -30
echo "(סה\"כ קבצים במצב לא-נקי: $(git status --porcelain | wc -l | tr -d ' '))"

echo ""
echo "===== 3. האם avraham-zadok כבר בגיט ====="
echo "קבצים במעקב תחת avraham-zadok/: $(git ls-files avraham-zadok | wc -l | tr -d ' ')"

echo ""
echo "===== 4. שלוש הקומיטים האחרונים ====="
git log --oneline -3

echo ""
echo "===== 5. הוספה, קומיט ודחיפה ====="
git add -A
git commit -m "הוספת מחקר אברהם צדוק (מהדורה 40) כתיקיית משנה avraham-zadok/" || echo "(אין מה לחייב — כנראה כבר חויב)"
BRANCH=$(git rev-parse --abbrev-ref HEAD)
echo "דוחף את הענף: $BRANCH"
git push origin "$BRANCH"
RC=$?
echo "קוד יציאה של git push: $RC"

echo ""
echo "===== 6. מקור GitHub Pages ====="
gh api "repos/ohadzad/ancestry-research/pages" 2>/dev/null \
  | python3 -c "import json,sys; d=json.load(sys.stdin); print('branch:', d['source']['branch'], '| path:', d['source']['path'], '| status:', d.get('status'))" \
  2>/dev/null || echo "(gh לא זמין או לא מחובר — דלג)"

echo ""
echo "===== סיום ====="
echo "אם קוד היציאה היה 0 — האתר יתעדכן תוך 1-2 דקות."
