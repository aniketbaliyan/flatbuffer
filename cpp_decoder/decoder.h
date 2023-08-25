#ifndef DECODER_H_
#define DECODER_H_

#include "schema_generated.h"
#include<iostream>
#include<fstream>

class decoder{
    public:
    uint8_t * getFileBuffer(std::string filename);
    void deserializeClient(std::string filename);
    void deserializePerson(const Schema::Client *client);
    void deserializeGroup(const Schema::Client *client);
};

#endif