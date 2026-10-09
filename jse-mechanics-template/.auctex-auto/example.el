;; -*- lexical-binding: t; -*-

(TeX-add-style-hook
 "example"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("revtex4-2" "amsmath" "amssymb" "aps" "endfloats" "linenumbers")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("graphicx" "") ("amsmath" "") ("amssymb" "") ("amsfonts" "") ("dcolumn" "") ("bm" "") ("siunitx" "") ("booktabs" "") ("hyperref" "colorlinks" "allcolors=blue") ("cleveref" "") ("svg" "") ("fancyhdr" "")))
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "email")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "homepage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "setfloatlink")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "href")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (TeX-run-style-hooks
    "latex2e"
    "revtex4-2"
    "revtex4-210"
    "graphicx"
    "amsmath"
    "amssymb"
    "amsfonts"
    "dcolumn"
    "bm"
    "siunitx"
    "booktabs"
    "hyperref"
    "cleveref"
    "svg"
    "fancyhdr")
   (TeX-add-symbols
    "blfootnote")
   (LaTeX-add-labels
    "fig:tart"
    "Equation 1. Horizontal component of projectile motion"
    "Equation 2. Vertical component of projectile motion"
    "Equation 3. Model of horizontal displacement"
    "tab:projectile-distance")
   (LaTeX-add-bibliographies)
   (LaTeX-add-pagestyles
    "mytitlepage"))
 :latex)

