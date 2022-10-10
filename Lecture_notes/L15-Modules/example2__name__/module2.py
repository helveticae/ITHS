import numpy as np

def trigonometric_identity(angle: float) -> float:
    """Calculates trigometric identity
    
        param:
        angle: angle in radians
        
        return trigometric one
    """
    print("Running trigometric_identity()")
    return np.cos(angle) ** 2 + np.sin(angle) **2

if __name__ == "__main__":
    print("Running from module2.py")
    print(trigonometric_identity(42))