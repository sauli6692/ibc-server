export const StringParsers: any = {
    capitalizeFirstLetter(word: string) {
        return word.charAt(0).toUpperCase() + word.slice(1).toLowerCase();
    }
};
