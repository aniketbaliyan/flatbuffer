Welcome to flatbuffer encoder and decoder
The repo contains a flatbuffer encoder in python and decoder in c++

recuirements to generate a flatbuffer encoded message with python repo
1 -> make sure you have flatc installed in your comp as per flatbuffer repo 
2 -> install python flatbuffer package present in flatbuffer repo

From main directory
Generate python schema files 
flatbuffers/flatc --python -o python_encoder schema/schema.fbs

Generate cpp schema files
flatbuffers/flatc --cpp -o cpp_decoder schema/schema.fbs

Encode in python
python3 encode.py file_name(where to dump the binary file)

Decode in cpp
1 - compile the executable
g++ main.cpp decoder.cpp -I path_to_flatbuffer_include_headers -std=c++11
2 - run the executable
./a.out path_to_binary_file
