const Model = () => {

}


[1,2]
[3,5]


const modelList = [new Model()]


const readFromLog = () => {
    const raw = []
    return raw
}

const injectModel = raw => {
    const modelList = []
    for(let i=0; i<raw.length; i+=1){
        const model = new Model(i)
        modelList.push(model)
    }
    return modelList;
}

const BASE_PATH = true?'/':'./'


