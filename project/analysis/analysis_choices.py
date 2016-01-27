AGE = (
	('18 - 21', '18 - 21'),
	('21 - 25', '21 - 25'),
	('25 - 35', '25 - 35'),
	('35 - 40', '35 - 40'),
	('40 - 45', '40 - 45'),
	('45 - 50', '45 - 50'),
	('50 - 55', '50 - 55'),
	('55 - 60', '55 - 60'),
	('60 - 65', '60 - 65'),
	('65 - 70', '65 - 70'),
	('70 - 75', '70 - 75'),
	('75+', '75+'),
)
MARITAL_STATUS = (
	('Single', 'Single'),
	('Married', 'Married'),
	('Separated', 'Separated'),
	('Divorced', 'Divorced'),
	('Widowed', 'Widowed'),
)
INCOME = (
	('$0 to $9,275', '$0 to $9,275'),
	('$9,275 to $37,650', '$9,275 to $37,650'),
	('$37,650 to $91,150', '$37,650 to $91,150'),
	('$91,150 to $190,150', '$91,150 to $190,150'),
	('$190,150 to #413,350', '$190,150 to #413,350'),
	('$413,350 to $415,050', '$413,350 to $415,050'),
	('$415,050+', '$415,050+'),
)
SAVING_RATE = (
	('10% to 15%', '10% to 15%'),
	('15% to 25%', '15% to 25%'),
	('25% to 35%', '25% to 35%'),
	('35% to 50%', '35% to 50%'),
	('50% to 60%', '50% to 60%'),
	('60% to 70%', '60% to 70%'),
	('70% to 80%', '70% to 80%'),
	('80%+', '80%+'),
)
FIXED_EXPENSES = (
	('10% to 15%', '10% to 15%'),
	('15% to 25%', '15% to 25%'),
	('25% to 35%', '25% to 35%'),
	('35% to 50%', '35% to 50%'),
	('50% to 60%', '50% to 60%'),
	('60% to 70%', '60% to 70%'),
	('70% to 80%', '70% to 80%'),
	('80%+', '80%+')
)
FEDERAL_TAX = (
	(10, '10%'),
	(15, '15%'),
	(25, '25%'),
	(28, '28%'),
	(33, '33%'),
	(35, '35%'),
	(39.6, '39.6%')
)
STATE_TAX = (
	(0, '0.00%'),
	(1, '1.00%'),
	(1.40, '1.40%'),
	(1.50, '1.50%'),
	(1.75, '1.75%'),
	(2, '2.00%'),
	(2.50, '2.50%'),
	(3, '3.00%'),
	(3.50, '3.50%'),
	(4, '4.00%'),
	(4.50, '4.50%'),
	(5, '5.00%'),
	(5.25, '5.25%'),
	(5.50, '5.50%'),
	(5.90, '1.90%'),
	(6, '6.00%'),
	(6.37, '6.37%'),
	(6.50, '6.50%'),
	(6.85, '6.85%'),
	(7, '7.00%'),
	(7.50, '7.50%'),
	(7.85, '.85%'),
	(8, '8.00%'),
	(8.50, '8.50%'),
	(8.97, '8.97%'),
	(9, '9.00%'),
	(9.50, '9.50%'),
	(10, '10.00%'),
	(10.50, '10.50%'),
	(11, '11.00%'),
)
CASH_RESERVES = (
	(1, 'Less than two months.'),
	(2, 'Two to three months.'),
	(3, 'Three to five months.'),
	(4, 'Six months or more.'),
)
TIME_HORIZONT = (
	(1, 'Five years or less.'),
	(2, 'Six to ten years.'),
	(3, 'Ten to fifteen years.'),
	(4, 'Greater than fifteen years.'),
)
MARKET_LOSS = (
	(1, 'None.'),
	(2, '5% or less.'),
	(3, '10% or less.'),
	(4, 'It does not matter as long as the investments are appropriate for my objective.'),
)
INVESTMENT_EXPERIENCE = (
	(1, 'None.'),
	(2, 'I have little background in purchasing stocks, some mutual funds.'),
	(3, 'I am comfortable with purchasing mutual funds, bonds, and stocks.'),
	(4, 'I have extensive investment experience with mutual funds, bonds, stocks, and derivatives.'),
)
INVESTMENT_RETURN = (
	(1, 'Less than half of the market, however preserving capital is my primary goal.'),
	(2, 'Half of the market but protecting against potential losses by a riskier portfolio is not preferred.'),
	(3, '15-20% by accepting a sufficient amount of risk.'),
	(4, 'More than 20% by investing in an investment portfolio more risky than the market.'),
)
GOAL_SHORT = (
	('Growth of Capital', 'Growth of Capital'),
	('Safty and preservation of capital', 'Safty and preservation of capital'),
	('Interest and Dividend Income', 'Interest and Dividend Income'),
	('Have Financial House in order', 'Have Financial House in order'),
	('Saving for Big purchase', 'Saving for Big purchase'),
	('Pay off Debt', 'Pay off Debt'),
	('Saving for Education', 'Saving for Education'),
	('Financial Freedom', 'Financial Freedom'),
	('Start own Business', 'Start own Business'),
	('Preparing for a life milestone', 'Preparing for a life milestone'),
	('Start to Do Work that I Love', 'Start to Do Work that I Love'),
	('Tax minimization', 'Tax minimization'),
	('Charitable giving', 'Charitable giving'),
	('Saving for Retirement', 'Saving for Retirement'),
	('Taking time off work', 'Taking time off work'),
	('Create additional Income streams', 'Create additional Income streams'),
	('Charitable giving', 'Charitable giving'),
	('Preparing for a life milestone', 'Preparing for a life milestone'),
)
GOAL_MID = (
	('Growth of Capital', 'Growth of Capital'),
	('Safty and preservation of capital', 'Safty and preservation of capital'),
	('Interest and Dividend Income', 'Interest and Dividend Income'),
	('Have Financial House in order', 'Have Financial House in order'),
	('Saving for Big purchase', 'Saving for Big purchase'),
	('Pay off Debt', 'Pay off Debt'),
	('Saving for Education', 'Saving for Education'),
	('Financial Freedom', 'Financial Freedom'),
	('Start own Business', 'Start own Business'),
	('Preparing for a life milestone', 'Preparing for a life milestone'),
	('Start to Do Work that I Love', 'Start to Do Work that I Love'),
	('Tax minimization', 'Tax minimization'),
	('Charitable giving', 'Charitable giving'),
	('Saving for Retirement', 'Saving for Retirement'),
	('Taking time off work', 'Taking time off work'),
	('Create additional Income streams', 'Create additional Income streams'),
	('Charitable giving', 'Charitable giving'),
	('Preparing for a life milestone', 'Preparing for a life milestone'),
)
GOAL_LONG = (
	('Saving for Retirement', 'Saving for Retirement'),
	('Saving for Education', 'Saving for Education'),
	('Start own Business', 'Start own Business'),
	('Preparing for a life milestone', 'Preparing for a life milestone'),
	('Start to Do Work that I Love', 'Start to Do Work that I Love'),
	('Tax minimization', 'Tax minimization'),
	('Charitable giving', 'Charitable giving'),
	('Preparing for a life milestone', 'Preparing for a life milestone'),
)
LIQIDITY_NEEDS = (
	('None for 6 monts', 'None for 6 monts'),
	('None for 12 monts', 'None for 12 monts'),
	('None for 1-2 years', 'None for 1-2 years'),
	('None for 3-5 years', 'None for 1-2 years'),
	('None for 10 years', 'None for 10 years'),
	('None for 10+ years', 'None for 10+ years'),
	)
TIME_RETIREMENT = (
	('35+ years', '35+ years'),
	('25+ years', '25+ years'),
	('15+ years', '15+ years'),
	('10+ years', '10+ years'),
	('5+ years', '5+ years'),
)







