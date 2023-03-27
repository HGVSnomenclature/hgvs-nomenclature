# random command lines used during processing

- replace `<b>...</b>` with `**...**` 

perl -i -pe 'm/<td/ or  s%<b>(.+?)</b>%**\1**%g' docs/**/*.md
perl -i -p0e 's%<i>(.+?)</i>%*\1*%g' docs/**/*.md




replace **"..."** and "**..**" blocks with **...**
