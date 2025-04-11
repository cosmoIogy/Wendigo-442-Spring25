import java.lang.reflect.Field;
import java.lang.reflect.Method;

public class InspectFields {
	public static void main(String[] args) throws Exception {
	
	Field[] fields = Hint.class.getDeclaredFields();
	Method[] methods = Hint.class.getDeclaredMethods();

	Class<Hint> tc = Hint.class;
	Hint testInstance = new Hint();

	for (Field field : fields) {
		field.setAccessible(true);
		System.out.println(field);
	}
	for (Method method : methods) {
		method.setAccessible(true);
		System.out.println(method);
	}

	fields[0].setAccessible(true);
	String s = fields[0].get(testInstance).toString();
	System.out.println(s);
	fields[0].set(testInstance, 1028);

	Method method1 = tc.getDeclaredMethod("superprivatefunction");
	method1.setAccessible(true);
	method1.invoke(testInstance);

	}
}
