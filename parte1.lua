function modPow(a, b, c)

    if (c <2 or a < 0 or b < 0) then error("valores invalidos de entrada") end
    return modPowRec(a,b,c)
end

function modPowRec(a,b,c)
    if b == 0 then
        return 1
    end

    return ( a%c * modPowRec(a,b-1,c) ) % c
end

function prodMat(A, B)

    AB = {}
    for i=1,#A do
        AB[i] = {}
        for j=1,#B[1] do
            ABij = 0
            for k=1,#B do
                ABij = ABij + A[i][k] * B[k][j]
            end
            AB[i][j] = ABij
        end
    end

    return AB
end

--4
print(modPow(2,5,7))

A = {
    {2,1,4},
    {0,1,1}
}

B = {
    {6,3,-1,0},
    {1,1,0,4},
    {-2,5,0,2}
}

AB = prodMat(A,B)



-- 5, 27, -2, 12
-- -1, 6, 0, 6
for i=1,#AB do
    print(table.concat(AB[i],", "))
end
