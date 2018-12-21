for files in /Users/py/GitHub/Float-Error-Neural-Network/cpp_bc/*.bc
do
  iconv -f binary -t UTF-8 "$files" "${files%.xxx}-utf8.bc"
done