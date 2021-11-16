for i in *
do
[ -d "$i" ] && zip -r "$i.zip" "$i"
rm -rf "$i"
done

