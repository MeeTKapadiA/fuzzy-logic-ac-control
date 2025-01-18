# fuzzy-logic-ac-control
A fuzzy logic system for air conditioner temperature control.

# Fuzzy Logic for Air Conditioner Temperature Control

This project demonstrates a fuzzy logic-based system to control the cooling power of an air conditioner. Using fuzzy logic, the system adjusts the AC power level based on the current room temperature and the desired temperature set by the user.

## Features
- Input variables:
  - **Room Temperature**: The current temperature of the room.
  - **Desired Temperature**: The temperature set by the user.
- Output variable:
  - **AC Power Level**: Adjusts cooling power (Low, Medium, High).
- Visualizes fuzzy membership functions and results using `matplotlib`.

## How It Works
1. **Fuzzy Membership Functions**:
   - Room Temperature: Cold, Comfortable, Hot.
   - Desired Temperature: Low, Medium, High.
   - AC Power Level: Low, Medium, High.
2. **Fuzzy Rules**:
   - If the room temperature is cold and the desired temperature is low, the AC power is low.
   - If the room temperature is hot and the desired temperature is high, the AC power is high.
   - Similar rules handle other combinations.
3. **Simulation**:
   - The system computes the AC power level using the fuzzy rules and visualizes the results.

## Requirements
Install the necessary libraries using:
```bash
pip install -r requirements.txt
```

### Required Libraries
- `scikit-fuzzy`
- `matplotlib`
- `numpy`

## How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/fuzzy-logic-ac-control.git
   ```
2. Navigate to the project directory:
   ```bash
   cd fuzzy-logic-ac-control
   ```
3. Run the Python script:
   ```bash
   python ac-temp.py
   ```

## Example Output
- Input:
  - Room Temperature: 30°C
  - Desired Temperature: 22°C
- Output:
  - AC Power Level: 8.27 (Medium-High)

The program also visualizes the membership functions and the computed result.

## License
This project is licensed under the MIT License. Feel free to use and modify it.

## Acknowledgments
- Developed using the `scikit-fuzzy` library.
- Inspired by real-world applications of fuzzy logic in HVAC systems.


## OUTPUT
AC Power Level: 8.269841269841269
![image](https://github.com/user-attachments/assets/4f9cc89d-450a-477d-94a2-36a9c68df8e8)
![image](https://github.com/user-attachments/assets/a83078ad-acc3-479c-a45b-a05e3623365d)
![image](https://github.com/user-attachments/assets/7889c198-494f-49ba-8883-7994a87b53dd)

