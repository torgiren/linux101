index.html: linux_101.md
	#pandoc linux_101.md -i -s  -o index.html -t revealjs
	pandoc linux_101.md -i -s  -o index.html -t revealjs  --template template.html -L revealjs-codeblock.lua -F r-stack-filter.py -V width=1200
