for i in *
do
cd "$i"
mv *\[YTS.*.srt "$i"-kimamastream.rf.gd.srt
mv *\[YTS.*.mp4 "$i"-kimamastream.rf.gd.mp4
mv *\[YTS.*.mkv "$i"-kimamastream.rf.gd.mkv

mv *YIFY.srt "$i"-kimamastream.rf.gd.srt
mv *YIFY.mp4 "$i"-kimamastream.rf.gd.mp4
mv *YIFY.mkv "$i"-kimamastream.rf.gd.mkv
cd ..
done

