export namespace MyMeal {
	export enum Type {
		first_meal = 0,
		second_meal = 1,
		salad = 2,
		drink = 3,
	}
	export const TypeMap = new Map<Type, string>([
		[Type.first_meal, 'soup'],
		[Type.second_meal, 'main_course'],
		[Type.salad, 'salad'],
		[Type.drink, 'drinks'],
	]);

	export interface Item {
		type: Type;
		name: string;
	}
	export const MyMealDictionary: Item[] = [
		{
			type: Type.first_meal,
			name: 'Суп гречаний',
		},
		{
			type: Type.first_meal,
			name: 'Окрошка',
		},
		{
			type: Type.first_meal,
			name: 'Борщ',
		},
		{
			type: Type.first_meal,
			name: 'Солянка',
		},
		{
			type: Type.second_meal,
			name: 'Галушки по-полтавські',
		},
		{
			type: Type.second_meal,
			name: "'Деруни з м'ясом",
		},
		{
			type: Type.second_meal,
			name: 'Картопляне пюре з відбивною',
		},
		{
			type: Type.second_meal,
			name: 'Зрази ',
		},
		{
			type: Type.second_meal,
			name: "Вареники з м'ясом",
		},
		{
			type: Type.second_meal,
			name: 'Плов з яловичиною ',
		},
		{
			type: Type.salad,
			name: 'Цезар ',
		},
		{
			type: Type.salad,
			name: 'Оселедець під шубою ',
		},
		{
			type: Type.salad,
			name: "Олів'є",
		},
		{
			type: Type.salad,
			name: 'Печінковий ',
		},
		{
			type: Type.salad,
			name: 'Салат зі свіжих овочей',
		},
		{
			type: Type.salad,
			name: 'Веган',
		},
		{
			type: Type.drink,
			name: 'Узвар ',
		},
		{
			type: Type.drink,
			name: 'Морс ',
		},
		{
			type: Type.drink,
			name: 'Пепсі',
		},
		{
			type: Type.drink,
			name: 'Холодний чай',
		},
	];
	// }
	// const randomFirstMeal = function () {
	// 	const first_meal = Object.keys(MyMeal.Type.first_meal);
	// 	first_meal[];
}
// const first_meal = MyMeal.MyMealDictionary[]
// console.log(MyMeal.MyMealDictionary[(Math.floor(Math.random() * MyMeal.MyMealDictionary.length))]);
const first_meal =
	MyMeal.MyMealDictionary[
		Math.floor(Math.random() * MyMeal.MyMealDictionary.length)
	];
const first_meal_name = first_meal.name;

console.log(first_meal_name);
