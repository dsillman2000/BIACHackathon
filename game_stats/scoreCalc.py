def scoreCalculator(kills, assists, deaths, dragons, barons):
    return (5 * kills) + (4 * assists) - (8 * deaths) + (3 * dragons) + (3 * barons)
