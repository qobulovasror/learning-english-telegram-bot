import React from 'react'

export default function FinallyScore() {
  return (
    <Card className="w-full max-w-md mx-auto">
      <CardHeader>
        <CardTitle>Quiz Completed!</CardTitle>
      </CardHeader>
      <CardContent>
        <p className="text-lg">Your score: {score} out of {quizSettings.questionCount}</p>
        <p>Category: {categories.find(cat => cat.value === quizSettings.category).label}</p>
        <p>Time taken: {quizSettings.timeLimit - timeLeft} seconds</p>
      </CardContent>
      <CardFooter>
        <Button onClick={resetQuiz}>Start New Quiz</Button>
      </CardFooter>
    </Card>
  );
}


