"""Smoke test — verifies all 37 SWC rules load and the scanner runs."""
from vulnerability_rules import VULNERABILITY_RULES
from scanner import scan_solidity

assert len(VULNERABILITY_RULES) == 37, f"Expected 37 rules, got {len(VULNERABILITY_RULES)}"
print(f"Rules loaded: {len(VULNERABILITY_RULES)}")

# Print all rule IDs
for r in VULNERABILITY_RULES:
    print(f"  {r['id']}  [{r['severity']:6}]  {r['name']}")

# Deliberately vulnerable contract
SAMPLE = """
pragma solidity ^0.6.0;

contract VulnerableAll {
    uint256 balance;
    address private secretKey = 0x0;
    mapping(address => uint) funds;

    function withdraw(uint amount) {
        require(balances[msg.sender] >= amount);
        msg.sender.call{value: amount}("");
        balance -= amount;
    }

    function kill() public { selfdestruct(msg.sender); }

    function rng() public view returns(uint) {
        return uint(blockhash(block.number - 1));
    }

    function auth() public view returns(bool) {
        return tx.origin == msg.sender;
    }

    function transferAll() public {
        msg.sender.transfer(address(this).balance);
    }

    function multiInherit() public {}
}

contract Child is VulnerableAll, Base {}
"""

result = scan_solidity(SAMPLE)
print(f"\nFindings: {result['total']}  |  Safe: {result['safe']}")
print(f"Summary : {result['summary']}")
print("\nPASS")
