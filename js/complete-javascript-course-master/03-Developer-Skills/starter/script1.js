// Remember, we're gonna use strict mode in all scripts now!
'use strict';
exports.__esModule = true;
exports.MyMeal = void 0;
// const measurementKelvin = function () {
// 	const measurement = {
// 		type: 'temp',
// 		unit: 'celsius',
// 		// FIX
// 		// value: Number(prompt('Degrees celsius:')),
// 		value: 15,
// 	};
// 	console.log(measurement);
// 	// B) FIND
// 	console.table(measurement);
// 	// console.log(measurement.value);
// 	// console.warn(measurement.value);
// 	// console.error(measurement.value);
// 	const kelvin = measurement.value + 273;
// 	return kelvin;
// };
// //A) IDENTIFY
// console.log(measurementKelvin());
// const calcTempAmplitudeBug = function (t1, t2) {
// 	const temps = t1.concat(t2);
// 	console.log(temps);
// 	let max = 0;
// 	let min = 0;
// 	for (let i = 0; i < temps.length; i++) {
// 		const curTemp = temps[i];
// 		if (typeof curTemp !== 'number') continue;
// 		if (curTemp > max) max = curTemp;
// 		if (curTemp < min) min = curTemp;
// 	}
// 	console.log(min, max);
// 	return max - min;
// };
// const amplitudeBug = calcTempAmplitudeBug([3, 5, 4], [10, 8, 2]);
// console.log(amplitudeBug);
// for (const [i, v] of ['a', 'b', 'c'].entries()) {
// 	console.log(i, v);
// }
// const temperatures = [17, 21, 23];
// const temperatures2 = [12, 5, -5, 0, 4];
// const printForecast = function (arr) {
// 	let str = '';
// 	for (const [i, element] of arr.entries()) {
// 		str = str + `${element}ºC in ${i + 1} days...`;
// 	}
// 	console.log('...' + str);
// };
// console.log(printForecast(temperatures));
// console.log(printForecast(temperatures2));
var rollNumberDate1 = function (min, max) {
	var random = new Date(
		Math.floor(
			Math.random() * (max.getTime() - min.getTime() + 1) + min.getTime()
		)
	);
	return random;
};
var minDate = new Date(Date.now() + Math.random());
minDate.setFullYear(new Date().getFullYear() - 19);
var maxDate = new Date(Date.now() + Math.random());
maxDate.setFullYear(new Date().getFullYear() - 46);
console.log(rollNumberDate1(minDate, maxDate));
var MyMeal;
(function (MyMeal) {
	var Type;
	(function (Type) {
		Type[(Type['first_meal'] = 0)] = 'first_meal';
		Type[(Type['second_meal'] = 1)] = 'second_meal';
		Type[(Type['salad'] = 2)] = 'salad';
		Type[(Type['drink'] = 3)] = 'drink';
	})((Type = MyMeal.Type || (MyMeal.Type = {})));
	MyMeal.TypeMap = new Map([
		[Type.first_meal, 'soup'],
		[Type.second_meal, 'main_course'],
		[Type.salad, 'salad'],
		[Type.drink, 'drinks'],
	]);
	MyMeal.MyMealDictionary = [
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
})((MyMeal = exports.MyMeal || (exports.MyMeal = {})));
const randomFirstMeal = function (MyMealDictionary) {
	var first_meal = Object.keys(MyMealDictionary.first_meal);
	first_meal[Math.floor(Math.random() * first_meal.length)];
};

console.log(randomFirstMeal());
