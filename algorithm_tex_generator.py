def figure_create_bst(f, idx):
    f.write("""
    \\begin{figure}[ht]
    \centering
    \\begin{tikzpicture}[y=0.80pt, x=0.80pt, yscale=1, xscale=1, inner sep=0pt, outer sep=0pt, 
    ->,>=stealth',shorten >=1pt,auto, thick, trans/.style={thick,->,>=stealth}]
      \\node[state, draw=none] (X)                    {};
    """)
    for i in range(10):
        for j in range(10):
            if j == 0:
                if i == 0:
                    f.write(f'\\node[state](I{i}{j})[below = 20 of X] {{{i}, {j}}};\n')
                else:
                    f.write(f'\\node[state](I{i}{j})[below = 20 of I{i - 1}{j}] {{{i}, {j}}};\n')
            else:
                f.write(f'\\node[state](I{i}{j})[right = 20 of I{i}{j - 1}] {{{i}, {j}}};\n')

    f.write('\\path\n')
    n = 10
    j = idx
    for i in range(1, n):
        for k in range(i, n - j):
            f.write(f'(I{i}{(k - 1)}) edge [bend right] node {{}} (I{i}{(i + j)})\n')
            f.write(f'(I{(k+1)}{(i + j)}) edge [bend right] node {{}} (I{i}{(i + j)})\n')
            f.write(f'(I{i}{(i + j)}) edge [bend right] node {{}} (I{i}{(i + j)})\n')
    # for (j = 1; j < n; j++)
    #     for (i=1; i < n-j; i++){
    #     for (k = i; k <= i+j; k++){
    #     w[i][i+j] = min(w[i][k-1] + w[k+1][i+j], w[i][i+j]);
    #     }
    #     for (k = i; k <= i+j; k++)
    #     w[i][i+j] += p[k];
    #     }

    f.write("""
;
\\end{tikzpicture}
\\label{fig:figure2}
\\end{figure}
    """)

def figure_create_if(f, idx):
    f.write("""
    \\begin{figure}[ht]
    \centering
    \\begin{tikzpicture}[y=0.80pt, x=0.80pt, yscale=1, xscale=1, inner sep=0pt, outer sep=0pt, 
    ->,>=stealth',shorten >=1pt,auto, thick, trans/.style={thick,->,>=stealth}]
      \\node[state, draw=none] (X)                    {};
    """)
    for i in range(10):
        for j in range(10):
            if j == 0:
                if i == 0:
                    f.write(f'\\node[state](I{i}{j})[below = 20 of X] {{{i}, {j}}};\n')
                else:
                    f.write(f'\\node[state](I{i}{j})[below = 20 of I{i - 1}{j}] {{{i}, {j}}};\n')
            else:
                f.write(f'\\node[state](I{i}{j})[right = 20 of I{i}{j - 1}] {{{i}, {j}}};\n')

    f.write('\\path\n')
    n = 10
    c0 = idx
    for c1 in range(1, n-c0):
        for c2 in range(c0+c1, min(n, 2 * c0 + c1 - 2)):
            if 2 * c0 + c1 >= c2 + 3:
                f.write(f'(I{c1}{(c2 - c0 + 1)}) edge [bend right] node {{}} (I{c1}{(c2)})\n')
                f.write(f'(I{(c2 - c0 + 1)}{c2}) edge [bend right] node {{}} (I{c1}{(c2)})\n')
            f.write(f'(I{c1}{(c0 + c1 - 1)}) edge [bend right] node {{}} (I{c1}{(c2)})\n')
            f.write(f'(I{(c0 + c1 - 1)}{c2}) edge [bend right] node {{}} (I{c1}{(c2)})\n')

    # c[c1][c2] = c[c1][c2 - c0 + 1] + c[c2 - c0 + 1][c2]
    # c[c1][c2] = c[c1][c0 + c1 - 1] + c[c0 + c1 - 1][c2]

    #   for (int c0 = 2; c0 < n; c0 += 1)
    #     for (int c1 = 1; c1 <= n - c0; c1 += 1)
    #       for (int c2 = c0 + c1; c2 <= min(n, 2 * c0 + c1 - 2); c2 += 1) {
    #         if (2 * c0 + c1 >= c2 + 3)
    #           S0(c0, c1, c2, -c0 + c2 + 1);
    #         S0(c0, c1, c2, c0 + c1 - 1);
    #       }
    #
    #
    #           S0( c1, c2, -c0 + c2 + 1);
    #     #         S0(c1, c2, c0 + c1 - 1);
    # p1 = c1 p2=c2 p3 = c2 - c0 + 1
    # c1, c2, -c0 + c2 + 1


    # #define S0(p1, p2, p3) c[p1][p2] = c[p1][p3] + c[p3][p2]


    f.write("""
;
\\end{tikzpicture}
\\label{fig:figure2}
\\end{figure}
    """)


with open('algo.tex', 'wt') as f:
    f.write("""
    \\documentclass{article}
    \\usepackage[utf8]{inputenc}
    \\usepackage{pgf}
    \\usepackage{tikz}
    \\usetikzlibrary{arrows,automata,positioning}
    \\usepackage{polski}
    \\usepackage{amsmath}
    \\usepackage{amssymb}
    \\usepackage{amsfonts}
    \\begin{document}
    """)

    # for fig_i in range(1, 10):
    #     figure_create_bst(f, fig_i)
    for fig_i in range(2, 10):
        figure_create_if(f, fig_i)

    f.write('\\end{document}')
