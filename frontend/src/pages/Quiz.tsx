const Quiz = () => {
  return (
    <Card className="w-full max-w-md mx-auto">
      <CardHeader>
        <CardTitle>Question </CardTitle>
        <p>Time left: {timeLeft} seconds</p>
      </CardHeader>
      <CardContent>
        <p className="mb-4">{currentQuizQuestion.question}</p>
        <RadioGroup onValueChange={handleAnswerSelection} value={selectedAnswer}>
          {currentQuizQuestion.options.map((option, index) => (
            <div key={index} className="flex items-center space-x-2 mb-2">
              <RadioGroupItem value={option} id={`option-${index}`} />
              <Label htmlFor={`option-${index}`}>{option}</Label>
            </div>
          ))}
        </RadioGroup>
      </CardContent>
      <CardFooter>
        <Button onClick={handleNextQuestion} disabled={!selectedAnswer}>
          {currentQuestion + 1 === quizSettings.questionCount ? 'Finish' : 'Next'}
        </Button>
      </CardFooter>
    </Card>
  );
};

export default Quiz;