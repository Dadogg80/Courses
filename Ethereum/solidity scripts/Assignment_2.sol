import "./Ownable.sol";
import "./Destroyable.sol";
pragma solidity 0.5.12;


contract HelloWorld is Ownable, Destroyable {

    struct Person {
        // Struct is used as in C++ to define our own datastructure.
        string name;
        uint age;
        uint height;
        string gender;
        bool senior;
    }

    event PersonCreated(string name, bool senior);
    event PersonDeleted(string name, bool senior, address deletedBy);

    uint public balance;

    modifier costs(uint cost) {
        require(msg.value >= cost);
        _;
    }

    mapping(address => Person) private people;
        // defines a mapping with (KEY address to VALUE Person) and call it people
    address[] private creators;

    function createPerson(string memory name, uint age, uint height, string memory gender)
    public payable costs(1 ether) {
        require(age < 120, "Age needs to be under 120 years.");
        balance += msg.value;

        Person memory newPerson;
        newPerson.name = name;
        newPerson.age = age;
        newPerson.height = height;
        newPerson.gender = gender;

        if (age >= 65) {
        //  if statement
            newPerson.senior = true;
        } else {
            // else statement
            newPerson.senior = false;
        }
        insertPerson(newPerson);
        creators.push(msg.sender);
    }

    function getPerson() public view returns(string memory name, uint age, uint height, string memory gender,
    bool senior) {
        address creator = msg.sender;
        // This function returns the person from the mapping
        return (people[creator].name, people[creator].age, people[creator].height, people[creator].gender,
    people[creator].senior);
    }

    function deletePerson(address creator) public onlyOwner {
        delete people[creator];
        assert(people[creator].age == 0);
    }

    function getCreator(uint index) public view onlyOwner returns(address) {
        return creators[index];
    }

    function withdrawAll() public onlyOwner returns(uint) {
        uint toTransfer = balance;
        balance = 0;
        msg.sender.transfer(toTransfer);
        return toTransfer;
    }

    function insertPerson(Person memory newPerson) private {
        address creator = msg.sender;
        people[creator] = newPerson;
        // initialise mapping to key = value
    }


}
