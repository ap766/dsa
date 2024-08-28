package extra.JavaOOPs;
class DemoBoxWeight{
    public static void main(String args[]) {
    BoxWeight mybox1 = new BoxWeight(10, 20, 15, 34.3);
    BoxWeight mybox2 = new BoxWeight(2, 3, 4, 0.076);
    double vol;
    vol = mybox1.volume();
    System.out.println("Volume of mybox1 is " + vol);
    System.out.println("Weight of mybox1 is " + mybox1.weight);
    System.out.println();
    vol = mybox2.volume();
    System.out.println("Volume of mybox2 is " + vol);
    System.out.println("Weight of mybox2 is " + mybox2.weight);
    }
    }


    // class DemoSuper {
    //     public static void main(String args[]) {
    //     BoxWeight mybox1 = new BoxWeight(10, 20, 15, 34.3);
    //     BoxWeight mybox2 = new BoxWeight(2, 3, 4, 0.076);
    //     BoxWeight mybox3 = new BoxWeight(); // default
    //     BoxWeight mycube = new BoxWeight(3, 2);
    //     BoxWeight myclone = new BoxWeight(mybox1);
    //     double vol;
    //     vol = mybox1.volume();
    //     System.out.println(&quot;Volume of mybox1 is &quot; + vol);
    //     System.out.println(&quot;Weight of mybox1 is &quot; + mybox1.weight);
    //     System.out.println();
    //     vol = mybox2.volume();
    //     System.out.println(&quot;Volume of mybox2 is &quot; + vol);
    //     System.out.println(&quot;Weight of mybox2 is &quot; + mybox2.weight);
    //     System.out.println();
    //     vol = mybox3.volume();
    //     System.out.println(&quot;Volume of mybox3 is &quot; + vol);
    //     System.out.println(&quot;Weight of mybox3 is &quot; + mybox3.weight);
    //     System.out.println();
    //     vol = myclone.volume();
    //     System.out.println(&quot;Volume of myclone is &quot; + vol);
    //     System.out.println(&quot;Weight of myclone is &quot; + myclone.weight);
    //     System.out.println();
    //     vol = mycube.volume();
    //     System.out.println(&quot;Volume of mycube is &quot; + vol);
    //     System.out.println(&quot;Weight of mycube is &quot; + mycube.weight);
    //     System.out.println();