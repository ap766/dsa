public class FirstPositionElement {
    public static void main(String[] args) {
        int[] arr = {5, 2, 7, 2, 9, 5, 7}; // Example array

        int firstPositionElement = arr[0]; // Get the element at first position

        int memoryAddress = System.identityHashCode(arr[0]); // Get the memory address of the first element

        System.out.println("Element at first position: " + firstPositionElement);
        System.out.println("Memory address of the first element: " + memoryAddress);
    }
}