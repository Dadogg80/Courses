pragma solidity 0.5.12;


// All Solidity contracts starts with contract and it´´s name.
contract TESTContract {

    // Struct is used as in C++ to define our own datastructure.
    struct Person {
        uint id;
        string name;
        uint age;
        uint height;
        string gender;
    }

    // Creates an public array named people.
    Person[] public people;

    // Function that creates a newPerson and adds it to the people array.
    function createPerson(string memory name, uint age, uint height, string memory gender) public {
        Person memory newPerson;
        newPerson.id = people.length;
        newPerson.name = name;
        newPerson.age = age;
        newPerson.height = height;
        newPerson.gender = gender;
        people.push(newPerson);

        /*  it´s possible to do the same as above with this line of code instead.

        people.push(Person(people.length, name, age, height, gender));

        */
    }



}
