# PyFincome: Fixed Income Valuation Solvers

Welcome to PyFincome, a Python repository dedicated to providing solvers for various topics discussed around Fixed Income valuations. This project is designed to aid in the study and understanding of fixed income securities as covered in courses like MGT 4068 or similar. Our aim is to build a collection of solvers for equations essential to the field of Fixed Income Securities, offering a practical tool for students, academics, and professionals alike.

## Topics Covered

PyFincome focuses on a wide range of topics within fixed income valuations, including but not limited to:

- **Interest Rates**: Calculation of simple and continuous compounding.
- **Bond Pricing**: Utilizing the discounted cash flow method to determine bond prices.
- **Forward Rates**: Understanding simple and continuous compounding in the context of forward rates.
- **Yield to Maturity**: Calculations for both simple (annual) compounding and continuous-compounding scenarios.
- **Hedging with Duration and Convexity**: Tools for managing interest rate risk.
- **Forward and Futures Price**: Determining the fair price for forward contracts.

## Featured Solvers

1. **Interest Rate Calculations**:
    - Simple Compounding: `A * (1 + R * T)`
    - Continuous Compounding: `A * exp(R * T)`

2. **Bond Price (Discounted Cash Flow Method)**:
    - For simple compounding: `PV(Bond) = sum(CF_t / (1 + Rs(0, t))**t for t in range(1, T+1))`
    - For continuous compounding: `PV(Bond) = sum(CF_t * exp(-Rc(0, t) * t) for t in range(1, T+1))`

3. **Forward Rates**:
    - For simple compounding: `f(0, T, T*) = ((1 + R(0, T*))**T* / (1 + R(0, T))**T)**(1 / (T* - T)) - 1`
    - For continuous compounding: `f(0, T, T*) = R(0, T*) + (R(0, T*) - R(0, T)) * (T / (T* - T))`

4. **Yield to Maturity**:
    - For simple compounding: `P = sum(CF_i / (1 + y)**i for i in range(1, n+1))`
    - For continuous compounding: `P = sum(CF_i * exp(-y * ti) for i in range(1, n+1))`
    
5. **Forward and Futures Pricing**:
    - For continuous compounding: `P_fwd_0 = B_0 * exp(R(0, T) * T)`
    - For simple compounding: `P_fwd_0 = B_0 * (1 + R(0, T))**T`

6. **Hedging with Duration**

- **First-order Taylor approximation of the change in bond price with respect to YTM**:  
  The change in the bond's price due to a small change in yield can be approximated by:  
  `∆P ≈ P'(y) * dy`  
  This formula represents a linear approximation of how the bond price responds to changes in the yield to maturity.

- **Dollar Duration**:  
  Represents the first derivative of the bond's price with respect to its yield, providing an estimate of how the price of a bond will change in response to a change in yield.
    - For simple compounding:  
      `$Dur = -sum([t * CF_t / (1 + y) ** (t + 1) for t in range(1, T+1)])`
    - For continuous compounding:  
      `$Dur = -sum([t * CF_t * exp(-y * t) for t in range(1, T+1)])`

- **Modified Duration (MD)**:  
  Measures the sensitivity of a bond's price to a change in yield, adjusting for the compounding frequency:  
  `MD = -P'(y) / P(y) = -∆P / (P * ∆y)`

- **Duration (D)**:  
  The weighted average time until a bond's cash flows are repaid, calculated as:  
  `D = 1 / P * sum([t * CF_t / (1 + y) ** t for t in range(1, T+1)])`

7. **Hedging with Convexity**

- **Dollar Convexity**:  
  Reflects the curvature of the price-yield relationship and the second derivative of the bond's price with respect to its yield.
    - For simple compounding:  
      `$Conv = sum([t * (t + 1) * CF_t / (1 + y) ** (t + 2) for t in range(1, T+1)])`
    - For continuous compounding:  
      `$Conv = sum([t**2 * CF_t * exp(-y * t) for t in range(1, T+1)])`

- **Relative Convexity**:  
  Normalizes dollar convexity by the bond's current price to provide a measure that is independent of the bond's size:  
  `Conv = $Conv / P`

- **Convexity of Portfolio (Convp)**:  
  The overall convexity of a portfolio, which takes into account the convexity of individual bonds weighted by their proportion in the portfolio:  
  `Convp = sum([Conv_i * weight_i for i in range(n)])`

## Getting Started

To get started with PyFincome, clone this repository and navigate to the individual solver directories for examples and usage instructions. Each solver comes with a detailed README explaining the underlying principles, assumptions, and how to use the solver for your calculations.

## Contribution

PyFincome is an open-source project, and contributions are welcome. Whether you'd like to add new solvers, improve existing ones, or contribute to the documentation, please feel free to fork the repository and submit your pull requests.

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for more details.

Thank you for exploring PyFincome, your companion for navigating the complexities of fixed income valuations!

## Contributors

- [Royden E. Daniels IV] - Author and maintainer of PyFincome.