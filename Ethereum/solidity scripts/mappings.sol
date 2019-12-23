pragma solidity 0.5.12;


// All Solidity contracts starts with contract and it´s name.
contract TESTContract {

    struct Person {
        // Struct is used as in C++ to define our own datastructure.
        string name;
        uint age;
        uint height;
        string gender;
    }

    mapping(address => Person) private people;
        // defines a mapping with (KEY address to VALUE Person) and call it people

    function createPerson(string memory name, uint age, uint height, string memory gender) public {
        address creator = msg.sender;

        // This function creates a person.
        Person memory newPerson;
        newPerson.name = name;
        newPerson.age = age;
        newPerson.height = height;
        newPerson.gender = gender;

        people[creator] = newPerson;
        // initialise mapping to key = value
    }

    function getPerson() public view returns(string memory name, uint age, uint height, string memory gender) {
        address creator = msg.sender;
        return (people[creator].name, people[creator].age, people[creator].height, people[creator].gender);
    }



}
