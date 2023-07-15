
Select *
From PortfolioProject1..deaths 
order by 3,4



	
--Select *
--From PortfolioProject..vac 
--order by 3,4

Select location, date, total_cases, new_cases, total_deaths, population 
From PortfolioProject1..deaths
order by 1,2

--Total cases vs Total death

Select Location, date, total_cases, total_deaths,  (cast(total_deaths as float)/ total_cases )*100 as deathpercentage
From PortfolioProject1..deaths
--Where location like '%india%' 
order by 1,2


--Total cases vs population
SET ARITHABORT OFF;
SET ANSI_WARNINGS OFF;
Select Location, date, population, total_cases, (total_cases /population)*100 as deathpercentage
From PortfolioProject1..deaths
--Where location like '%india%' 
order by 1,2

--Countries with highest cases
SET ARITHABORT OFF;
SET ANSI_WARNINGS OFF;
Select location, population, MAX(total_cases) as HighestInfectionCount , Max((total_cases /population ))*100 as PercentPopulationInfected
From PortfolioProject1..deaths
--Where location like '%states%'
where continent is not null
Group by location, population
order by PercentPopulationInfected desc 


--highest death count per population
Select Location,MAX(cast(total_deaths as int)) as death_count 
From PortfolioProject1..deaths
where continent is not null
Group by Location
order by death_count desc 

--global number

Select date, SUM(new_cases) as tota_cases,Sum(cast(new_deaths as int)) as total_deaths, Sum(cast(new_deaths as int))/SUM(new_cases)*100 as deathpercentage
From PortfolioProject1..deaths
--Where location like '%india%' 
Group by date
order by 1,2

--total population vs vaccination

Select d.continent,d.location, d.date, d.population, v.new_vaccinations  
, SUM(CONVERT(float,v.new_vaccinations )) OVER (Partition by d.location Order by d.location,d.date) as n_people_vaccinated
From PortfolioProject1..deaths d
Join PortfolioProject1..vac  v
 on d.location= v.location
 and d.date= v.date
 where d.continent is not null
 order by 2,3

 --use CTE
With popvsvac (continent, Location, date, population, new_vaccinations, n_people_vaccinated)
as
(
Select d.continent,d.location, d.date, d.population, v.new_vaccinations  
, SUM(CONVERT(float,v.new_vaccinations )) OVER (Partition by d.location Order by d.location,d.date) as n_people_vaccinated
From PortfolioProject1..deaths d
Join PortfolioProject1..vac  v
	On d.location= v.location
	and d.date= v.date
where d.continent is not null
)
Select *, (n_people_vaccinated /population )*100
From popvsvac where population != '0'
order by Location,date



DROP Table if exists #PercentPopulationVaccinated
Create Table #PercentPopulationVaccinated
(
Continent nvarchar(255),
Location nvarchar(255),
Date datetime,
Population numeric,
New_vaccinations numeric,
RollingPeopleVaccinated numeric
)
