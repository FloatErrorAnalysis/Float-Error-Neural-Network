#!/bin/bash 
find /Users/py/GitHub/Float-Error-Neural-Network/cpp_bc/ -type f | \ 
	(while read file ; do 
		if [[ "$file" != *.DS_Store* ]]; 
			then if [[ "$file" != *-utf8* ]];
			 then iconv -f CP1251 -t UTF-8 "$file" > "$file-utf8";
			  rm $file; mv "$file-utf8" "$file"; fi fi done);