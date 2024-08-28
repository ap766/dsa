package extra.JavaOOPs;

public class Bicycle {
    public int gear;
    public int speed;

    public Bicycle(int gear,int speed){
        this.gear = gear;
        this.speed = speed;
    }
    public void applybrake(int decrement){
        speed-=decrement;
    }
    public void speedUp(int increment){
        speed+=increment;
    }
    public String toString(){
        return ("No of gears are "+gear+"\n"+"speed of bicycle is "+speed);
    }
}
class MountainBike extends Bicycle {
    public int seatHeight;
     public MountainBike(int gear, int speed,
                        int startHeight)
    {
        // invoking base-class(Bicycle) constructor
        super(gear, speed);
        seatHeight = startHeight;
    }

    // the MountainBike subclass adds one more method
    public void setHeight(int newValue)
    {
        seatHeight = newValue;
    }

    @Override public String toString()
    {
        return (super.toString() + "\nseat height is "
                + seatHeight);
    }
}
