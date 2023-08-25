#include"decoder.h"

int main(int argc, char *argv[]){

    // std::fstream file;
    std::string filename = argv[1];

    decoder obj;
    obj.deserializeClient(filename);
    
    return 1;
}