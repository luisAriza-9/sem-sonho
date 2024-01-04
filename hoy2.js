function countPairs(projectCosts, target) {
    let count = 0;
    for (let i = 0; i < projectCosts.length; i++) {
        for (let j = i + 1; j < projectCosts.length; j++) {
            if (Math.abs(projectCosts[i] - projectCosts[j]) === target) {
                count++;
            }
        }
    }
    return count;
}
