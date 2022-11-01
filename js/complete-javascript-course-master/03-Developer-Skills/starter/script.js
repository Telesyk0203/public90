// Remember, we're gonna use strict mode in all scripts now!
'use strict';

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

function rollNumberDate(min, max) {
	const random = new Date(
		Math.floor(
			Math.random() * (max.getTime() - min.getTime() + 1) + min.getTime()
		)
	);
	return random;
}

const min = new Date(Date.now() + Math.random());
min.setFullYear(new Date().getFullYear() - 19);

const max = new Date(Date.now() + Math.random());
max.setFullYear(new Date().getFullYear() - 46);

// console.log(rollNumberDate(min, max));
