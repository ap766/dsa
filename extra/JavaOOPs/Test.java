package extra.JavaOOPs;

public class Test {
    public static void main(String[] args) {
        Bicycle bicycle = new Bicycle(3, 100);
        System.out.println(bicycle.toString());

        MountainBike mountainBike = new MountainBike(3, 100, 25);
        System.out.println(mountainBike.toString());
    }
}
