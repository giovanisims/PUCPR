package aula12;

import java.util.ArrayList;
import java.util.Scanner;

public class pbl05 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Creating Students
        ArrayList<Person> payroll = getPeople();

        for (Person p : payroll){
            System.out.println(p.getName());
        }

        while (true) {
            System.out.println("""
                    
                    ********* Menu *********
                    (1) Ver detalhes do funcionário
                    (2) Sair
                    """);
            System.out.print("Opção: ");
            int option = sc.nextInt();
            sc.nextLine();

            switch (option) {
                case 1:
                    System.out.print("Digite o nome do funcionário: ");
                    String name = sc.nextLine();
                    if (!isNameInList(payroll, name)) {
                        System.out.println("Funcionário não encontrado.");
                        break;
                    }

                    boolean validInput = false;
                    while (!validInput) {
                        System.out.printf("Te certeza que deseja ver os dados do(a) %s? ", name);
                        String confirmation = sc.nextLine().toLowerCase();
                        switch (confirmation) {
                            case "sim":
                                displayEmployeeDetails(payroll, name);
                                validInput = true;
                                break;
                            case "não":
                                validInput = true;
                                break;
                            default:
                                System.out.println("Digite Sim ou Não");
                                break;
                        }
                    }

                    break;


                case 2:
                    System.out.println("Saindo...");
                    sc.close();
                    return;


                default:
                    System.out.println("Opção Inválida. Tente novamente.");
                    break;
            }
        }
    }

    private static ArrayList<Person> getPeople() {
        Student student1 = new Student("Alice", 20, "alice@example.com", "S001", "Computer Science");
        Student student2 = new Student("Bob", 22, "bob@example.com", "S002", "Mathematics");
        Student student3 = new Student("Charlie", 21, "charlie@example.com", "S003", "Physics");
        Student student4 = new Student("Diana", 23, "diana@example.com", "S004", "Chemistry");

        // Creating Teachers
        Teacher teacher1 = new Teacher("Eve", 40, "eve@example.com", 5000.0, "Biology");
        Teacher teacher2 = new Teacher("Frank", 45, "frank@example.com", 5500.0, "History");

        // Creating Employees
        Employee employee1 = new Employee("Grace", 30, "grace@example.com", "Admin", 40, 20.0);
        Employee employee2 = new Employee("Hank", 35, "hank@example.com", "Maintenance", 40, 15.0);
        Employee employee3 = new Employee("Ivy", 28, "ivy@example.com", "Library", 40, 18.0);
        Employee employee4 = new Employee("Jack", 32, "jack@example.com", "IT", 40, 25.0);
        Employee employee5 = new Employee("Karen", 29, "karen@example.com", "Cafeteria", 40, 12.0);

        // Creating Monitor
        Monitor monitor1 = new Monitor("Leo", 24, "leo@example.com", 20);

        // Makes list of everyone
        ArrayList<Person> payroll = new ArrayList<>();
        payroll.add(student1);
        payroll.add(student2);
        payroll.add(student3);
        payroll.add(student4);
        payroll.add(teacher1);
        payroll.add(teacher2);
        payroll.add(employee1);
        payroll.add(employee2);
        payroll.add(employee3);
        payroll.add(employee4);
        payroll.add(employee5);
        payroll.add(monitor1);
        return payroll;
    }

    public static void displayEmployeeDetails(ArrayList<Person> payroll, String name) {
        for (Person employee : payroll) {
            if (employee.getName().equalsIgnoreCase(name)) {
                System.out.println(employee);
            }
        }
    }

    public static boolean isNameInList(ArrayList<Person> payroll, String name) {
        for (Person employee : payroll) {
            if (employee.getName().equalsIgnoreCase(name)) {
                return true;
            }
        }
        return false;
    }

}


class Person {
    protected final String name;
    protected final String email;
    protected int age;

    protected Person(String name, int age, String email) {
        this.name = name;
        this.age = age;
        this.email = email;
    }

    public String getName() {
        return name;
    }

    public String toString() {
        return String.format("Nome: %s | Idade: %d | Email: %s", this.name, this.age, this.email);
    }
}

class Student extends Person {
    private final String studentID;
    private final String course;

    Student(String name, int age, String email, String studentID, String subject) {
        super(name, age, email);
        this.studentID = studentID;
        this.course = subject;
    }

    public String toString() {
        return String.format(super.toString(), "Matriucula: %s | Curso: %s ", this.studentID, this.course);
    }
}

class Teacher extends Person {
    private final String subject;
    private final double salary;

    Teacher(String name, int age, String email, double wage, String subject) {
        super(name, age, email);
        this.salary = wage;
        this.subject = subject;
    }

    public String toString() {
        return String.format(super.toString(), "Disciplina: %s | Salario: %s ", this.subject, this.salary);
    }

    public String bonus() {
        return String.format("Bônus: %.2f", (this.salary * 1.1));
    }
}

class Employee extends Person {
    private final String department;
    private final int workHours;
    private final double workSalary;

    Employee(String name, int age, String email, String department, int workHours, double workSalary) {
        super(name, age, email);
        this.department = department;
        this.workHours = workHours;
        this.workSalary = workSalary;
    }

    public String calculatePayment() {
        return String.format("Departamento: %s | O pagamento é: %.2f", this.department, this.workHours * this.workSalary);
    }
}

class Monitor extends Person {
    private final int workHours;

    Monitor(String name, int age, String email, int monitorHours) {
        super(name, age, email);
        this.workHours = monitorHours;
    }

    public String toString() {
        return String.format(super.toString(), "Horas de monitoria: %.2f", this.workHours);
    }

    public String calculatePayment() {
        return String.format("O pagamento é: %x", this.workHours * 30);
    }
}