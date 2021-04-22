(TeX-add-style-hook
 "Manual"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("report" "a4papper" "12pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("fontenc" "T2A") ("inputenc" "utf8") ("babel" "english" "russian")))
   (TeX-run-style-hooks
    "latex2e"
    "report"
    "rep12"
    "cmap"
    "fontenc"
    "inputenc"
    "babel"))
 :latex)

