const { RpcProvider } = require("starknet");

// Create a new instance of the default provider
const defaultProvider = new RpcProvider({
  nodeUrl:
    "https://starknet-mainnet.g.alchemy.com/v2/ekJheYMyUgzO8bxrMq0e6PCgir5WuJqK",
});

// Function to fetch and log the latest block information
async function fetchAndLogLatestBlock() {
  try {
    // Get the latest block
    const latestBlock = await defaultProvider.getBlock("latest");

    // Log specific details from the latest block
    console.log("Latest Block Details:");
    console.log(`Block Number: ${latestBlock.block_number}`);
    console.log(`Block Hash: ${latestBlock.block_hash}`);

    // Convert the StarkNet block timestamp to Unix timestamp in seconds
    const unixTimestampNow = Math.floor(
      new Date(latestBlock.timestamp * 1000).getTime() / 1000
    );
    console.log(`Current Unix Timestamp (seconds): ${unixTimestampNow}`);

    // Your target Unix timestamp
    const targetUnixTimestamp = 1708598922;
    const timeRemaining = targetUnixTimestamp - unixTimestampNow;

    // Convert the time remaining to a more readable format
    const hoursRemaining = Math.floor(timeRemaining / 3600);
    const minutesRemaining = Math.floor((timeRemaining % 3600) / 60);
    const secondsRemaining = timeRemaining % 60;

    console.log(
      `Time remaining until target timestamp: ${hoursRemaining} hours, ${minutesRemaining} minutes, ${secondsRemaining} seconds.`
    );
  } catch (error) {
    console.error("Error fetching the latest block:", error);
  }
}

// Function to start the polling process
function startPollingLatestBlock(interval = 10000) {
  // Immediately fetch the latest block information
  fetchAndLogLatestBlock();
  // Set up a repeated call to the function at the specified interval
  setInterval(fetchAndLogLatestBlock, interval);
}

// Start polling for the latest block information every 10 seconds
startPollingLatestBlock();
