package aula11;

public class Property01 {
    public static void main(String[] args) {
        Property newProperty = new NewProperty("Rua Nova, 123", 300000);
        Property oldProperty = new OldProperty("Rua Antiga, 456", 200000);

        System.out.println(newProperty);
        System.out.println(oldProperty);
    }
}

class Property {
    private final String address;
    private final double price;

    Property(String address, double price) {
        this.address = address;
        this.price = price;
    }

    public String getAddress() {
        return this.address;
    }

    public double getPrice() {
        return this.price;
    }

    @Override
    public String toString() {
        return "Endereço: " + this.address + ", Valor: " + this.price;
    }
}

class NewProperty extends Property {

    public NewProperty(String address, double price) {
        super(address, price);
    }

    public double getMarkup() {
        return (getPrice() * 1.1);
    }

    @Override
    public String toString() {
        return super.toString() + ", Valor com acréscimo: " + getMarkup();
    }
}

class OldProperty extends Property {

    public OldProperty(String address, double price) {
        super(address, price);
    }

    public double getDiscount() {
        return (getPrice() * 0.9);
    }

    @Override
    public String toString() {
        return super.toString() + ", Valor com desconto: " + getDiscount();
    }
}