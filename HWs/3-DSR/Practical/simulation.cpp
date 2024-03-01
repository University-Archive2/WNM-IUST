#include <iostream>
#include <random>
#include <vector>

using namespace std;

// Define the maximum number of nodes in the network
const int MAX_NODES = 100;

// Define the packet delivery success probability
double PACKET_SUCCESS_PROBABILITY;

// Define the latency for successful packet delivery
const int PACKET_LATENCY = 10;

// Define the latency for unsuccessful packet delivery
const int PACKET_LOSS_LATENCY = 50;

// Define the number of packets 
const int NUMBER_OF_PACKETS = 10000;

// Function to simulate a packet delivery attempt between two nodes
bool simulatePacketDelivery(int sender, int receiver, mt19937& rng) {
    // Generate a random number between 0 and 1
    uniform_real_distribution<double> dist(0, 1);
    double rand_num = dist(rng);

    // If the random number is less than the packet success probability,
    // the packet is successfully delivered
    if (rand_num < PACKET_SUCCESS_PROBABILITY) {
        return true;
    } else {
        return false;
    }
}

// Function to simulate the network
void simulateNetwork(int num_nodes, double& delivery_rate, double& avg_latency, mt19937& rng) {
    // Initialize the packet delivery count and total latency
    int delivery_count = 0;
    int total_latency = 0;

    // Loop over the number of packets to be sent
    for (int i = 0; i < num_nodes; i++)
        for (int j = 0; j < NUMBER_OF_PACKETS; j++) {
            // Select a random sender and receiver node
            int sender = rand() % num_nodes;
            int receiver = rand() % num_nodes;

            // Ensure that the sender and receiver nodes are different
            while (sender == receiver) {
                receiver = rand() % num_nodes;
            }

            // Simulate a packet delivery attempt between the sender and receiver nodes
            bool success = simulatePacketDelivery(sender, receiver, rng);

            // Update the packet delivery count and total latency
            if (success) {
                delivery_count++;
                total_latency += PACKET_LATENCY;
            } else {
                total_latency += PACKET_LOSS_LATENCY;
            }
        }

    // Compute the delivery rate and average latency
    delivery_rate = (double)delivery_count / (NUMBER_OF_PACKETS * num_nodes);
    avg_latency = (double)total_latency / (NUMBER_OF_PACKETS * num_nodes);
}

int main() {
    // Seed the random number generator with a random value from std::random_device
    random_device rd;
    mt19937 rng(rd());
    uniform_real_distribution<double> dist(0.6, 0.95);
    PACKET_SUCCESS_PROBABILITY = dist(rng);

    int num_nodes;
    cin >> num_nodes;


    // Simulate the network and compute the packet delivery rate and average latency
    double delivery_rate, avg_latency;
    simulateNetwork(num_nodes, delivery_rate, avg_latency, rng);
    // Print the results
    cout << delivery_rate << " " << avg_latency << endl;
}
