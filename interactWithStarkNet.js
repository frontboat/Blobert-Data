const { Contract, constants, RpcProvider } = require("starknet");
const fs = require("fs").promises;

(async () => {
  try {
    const provider = new RpcProvider({
      nodeUrl:
        "https://starknet-mainnet.g.alchemy.com/v2/ekJheYMyUgzO8bxrMq0e6PCgir5WuJqK",
    });

    const testAddress =
      "0x00539f522b29ae9251dbf7443c7a950cf260372e69efab3710a11bf17a9599f1";
    const { abi: testAbi } = await provider.getClassAt(testAddress);
    if (testAbi === undefined) throw new Error("no abi.");
    const myTestContract = new Contract(testAbi, testAddress, provider);

    let tokenId = BigInt(1);
    let traitsResults = [];

    while (true) {
      try {
        const traitResult = await myTestContract.traits(tokenId.toString());
        traitsResults.push({
          tokenId: tokenId.toString(),
          traits: traitResult,
        });
        console.log(`Fetched traits for token ID ${tokenId}`);
        tokenId++;
      } catch (error) {
        if (error.message.includes("invalid token ID")) {
          console.log(
            `Stopping fetch at token ID ${tokenId}: ${error.message}`
          );
          break;
        } else {
          console.error(
            `Error fetching traits for token ID ${tokenId}: ${error.message}`
          );
        }
      }
    }

    // Export the results to a file with proper BigInt handling
    await fs.writeFile(
      "traitsResults.json",
      JSON.stringify(
        traitsResults,
        (key, value) => {
          return typeof value === "bigint" ? value.toString() : value;
        },
        2
      )
    );
    console.log("Exported traits results to traitsResults.json");
  } catch (error) {
    console.error("Failed to initialize contract interaction:", error);
  }
})();
