# random command lines used during processing

- replace `<b>...</b>` with `**...**` 

perl -i -pe 'm/<td/ or  s%<b>(.+?)</b>%**\1**%g' docs/**/*.md
perl -i -p0e 's%<i>(.+?)</i>%*\1*%g' docs/**/*.md

- replace `[**...**]` with `[...]`

perl -i -p0e 's%\[\*\*(.+?)\*\*\]%[\1]%g' docs/**/*.md


- replace **"..."** and "**..**" blocks with **...**

- replace red font with span
perl -i -p0e 's%<font color="red">(.+?)</font>%<span class="spotlight">\1</span>%g' docs/**/*.md
