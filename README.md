# WGUPS Routing Program Implementation  

**Author:** Duvall Roberts  
**Course:** C950  

## Overview  
This program implements a **custom hash table** to efficiently manage package data and optimize delivery routes. The goal was to ensure that all deliveries are completed on time while keeping the total travel distance under 140 miles. This project demonstrates skills in data structures, algorithm design, and Python programming.

---

## Features  

### A. Hash Table Implementation  
- **Purpose:**  
  - The custom hash table supports **quick insertion** and **retrieval** of packages using their unique IDs.  
  - It handles package information efficiently while adhering to delivery constraints.  

- **Insertion Function:**  
  - Stores delivery address, deadlines, city, zip code, weight, and delivery status for each package.  
  - Allows fast updates and quick access to package details.  

- **Look-Up Function:**  
  - Queries the data associated with a specific package ID.  
  - Facilitates real-time tracking and status updates of deliveries.

---

### B. Look-Up Function Implementation  
- Accepts a **package ID** as input to return the relevant package details.  
- This function ensures that packages can be easily tracked through the delivery process.

---

### C. Program Implementation Details  
- **Language:** Python  
- **Code Structure:**  
  1. **Student ID Comment:** The first line of `main.py` includes the required student ID.  
  2. **Code Comments:** Thorough comments throughout the code explain the logic, data structures, and how routes are calculated.

---

### D. User Interface and Delivery Status  
- The program provides a **user-friendly interface** for monitoring delivery status.  
  - Displays real-time information on package delivery times and total mileage.  
  - Shows data for **D1 and D2 deliveries** for quick status verification.

---

### E. Total Mileage and Completion  
- Ensures that the **total mileage** traveled by all trucks remains under **140 miles**.  
- All deliveries are completed **before 12:03 p.m.**, meeting the delivery deadline.

---

### F. Algorithm Justification  
1. **Strengths:**  
   - **Efficiency:** Balances the load between three trucks, ensuring optimized routes.  
   - **Simplicity:** The algorithm is straightforward, easy to implement, and meets all project requirements.  
2. **Verification:**  
   - Ensured that all deliveries meet deadlines and total distance is within the required limit.  
3. **Alternative Algorithms:**  
   - **Nearest Neighbor Algorithm:** Focuses on minimizing travel distance but may not prioritize deadlines.  
   - **Genetic Algorithm:** Offers powerful route optimization but requires more computational resources.  

---

### G. Alternative Approaches  
- **Dynamic Route Optimization:** Could adapt routes in real time based on traffic or package availability.  
- **Machine Learning Integration:** Historical data could be used to further improve delivery routes and efficiency.

---

### H. Data Structure Verification  
1. **Verification:**  
   - The custom hash table meets the project requirements by enabling fast storage and retrieval of package information.  
2. **Alternative Data Structures:**  
   - **Binary Search Tree:** Faster for range queries but more complex to implement.  
   - **Linked List:** Simpler structure but may be slower for larger datasets.

---

## Conclusion  
The WGUPS Routing Program effectively manages package data using a custom hash table, ensuring all deliveries are made within the required deadlines while keeping total mileage under 140 miles. Through this project, various algorithmic and data structure techniques were explored, demonstrating practical applications in logistics and delivery optimization.

---

