#include"decoder.h"

using namespace Schema;
    
uint8_t * decoder::getFileBuffer(std::string filename){

    std::fstream file;
    
    file.open(filename, std::ios_base::in | std::ios_base::binary);
    auto file_size = std::__fs::filesystem::file_size(filename);
    
    uint8_t *data = reinterpret_cast<uint8_t *>(new int[file_size]);
    file.read(reinterpret_cast<char *>(data), file_size);

    return data;
}
    
void decoder::deserializeClient(std::string filename){
    
    uint8_t * data = getFileBuffer(filename);
    auto client = GetClient(data);

    auto client_data_type = client->client_data_type();

    if (client_data_type == Type_Person){
        deserializePerson(client);
    }    
    else if(client_data_type == Type_Group){
        deserializeGroup(client);
    }
    else{
        std::cout << "Unknown Type" <<"\n";
    }

}

void decoder::deserializePerson(const Schema::Client *client){
    
    auto person = static_cast<const Person*>(client->client_data());
    
    auto person_name = person->name()->c_str();
    auto person_age = person->age();
    auto person_weight = person->weight();
    auto person_gender = person->gender()->c_str();

    std::cout << person_name << "\n" << person_age << "\n" << person_weight << "\n" << person_gender<< "\n";
}

void decoder::deserializeGroup(const Schema::Client *client){
    auto group = static_cast<const Group*>(client->client_data());

    auto group_name = group->name()->c_str();
    auto group_age = group->age();
    auto group_weight = group->weight();
    
    std::cout << group_name << "\n" << group_age << "\n" << group_weight << "\n";
    
    auto group_list = group->list();

    auto group_size = group_list->size();

    for(int i=0;i<group_size;i++){
        std::cout << group_list->Get(i)->c_str() << "\n";
    }
}
