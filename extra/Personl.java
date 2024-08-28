package extra;

public class Personl {
    String name;
    Integer age;
    Personl(String n,Integer a){
        this.name=n;
        this.age=a;
    }

    public static void main(String[] args) {
        Personl p=new Personl("j",7);
        System.out.println(p.name);
    }
}
