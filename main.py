from core.eye_tracking import start_eye_tracking
from core.blink_detection import detect_blink
from ui.virtual_keyboard import launch_virtual_keyboard

def main():
    print("Starting AI-Powered Accessibility Tool...")
    
    # Start Eye Tracking
    start_eye_tracking()

    # Launch Virtual Keyboard
    launch_virtual_keyboard()

    # Detect blink gestures
    detect_blink()

if __name__ == "__main__":
    main()