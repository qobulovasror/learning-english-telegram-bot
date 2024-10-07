import React, { useState } from 'react';
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardFooter, CardHeader, CardTitle } from '@/components/ui/card';
import { RadioGroup, RadioGroupItem } from '@/components/ui/radio-group';
import { Label } from '@/components/ui/label';
import { Input } from '@/components/ui/input';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select';

const categories = [
  { value: 'general', label: 'General Vocabulary' },
  { value: 'business', label: 'Business English' },
  { value: 'academic', label: 'Academic English' },
  { value: 'idioms', label: 'Idioms and Phrases' },
];

const QuizSetup = ({ onStartQuiz }) => {
  const [timeLimit, setTimeLimit] = useState(60);
  const [questionCount, setQuestionCount] = useState(10);
  const [category, setCategory] = useState('general');

  const handleStartQuiz = () => {
    onStartQuiz({ timeLimit, questionCount, category });
  };

  return (
    <Card className="w-full max-w-md mx-auto">
      <CardHeader>
        <CardTitle>Quiz Setup</CardTitle>
      </CardHeader>
      <CardContent className="space-y-4">
        <div className="space-y-2">
          <Label htmlFor="time-limit">Time Limit (seconds)</Label>
          <Input
            id="time-limit"
            type="number"
            value={timeLimit}
            onChange={(e) => setTimeLimit(Number(e.target.value))}
            min={30}
            max={300}
          />
        </div>
        <div className="space-y-2">
          <Label htmlFor="question-count">Number of Questions</Label>
          <Input
            id="question-count"
            type="number"
            value={questionCount}
            onChange={(e) => setQuestionCount(Number(e.target.value))}
            min={5}
            max={50}
          />
        </div>
        <div className="space-y-2">
          <Label htmlFor="category">Category</Label>
          <Select value={category} onValueChange={setCategory}>
            <SelectTrigger id="category">
              <SelectValue placeholder="Select a category" />
            </SelectTrigger>
            <SelectContent>
              {categories.map((cat) => (
                <SelectItem key={cat.value} value={cat.value}>
                  {cat.label}
                </SelectItem>
              ))}
            </SelectContent>
          </Select>
        </div>
      </CardContent>
      <CardFooter>
        <Button onClick={handleStartQuiz}>Start Quiz</Button>
      </CardFooter>
    </Card>
  );
};

const QuizApp = () => {
  const [quizStarted, setQuizStarted] = useState(false);
  const [quizSettings, setQuizSettings] = useState(null);
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [selectedAnswer, setSelectedAnswer] = useState('');
  const [score, setScore] = useState(0);
  const [quizCompleted, setQuizCompleted] = useState(false);
  const [timeLeft, setTimeLeft] = useState(0);

  // Simulated quiz data - replace with actual data fetching based on category
  const quizData = [
    {
      question: "What is the capital of France?",
      options: ["London", "Berlin", "Paris", "Madrid"],
      correctAnswer: "Paris"
    },
    {
      question: "Which planet is known as the Red Planet?",
      options: ["Mars", "Venus", "Jupiter", "Saturn"],
      correctAnswer: "Mars"
    },
    // Add more questions here
  ];

  React.useEffect(() => {
    let timer: NodeJS.Timeout;
    if (quizStarted && timeLeft > 0) {
      timer = setTimeout(() => setTimeLeft(timeLeft - 1), 1000);
    } else if (timeLeft === 0 && quizStarted) {
      setQuizCompleted(true);
    }
    return () => clearTimeout(timer);
  }, [quizStarted, timeLeft]);

  const startQuiz = (settings) => {
    setQuizSettings(settings);
    setTimeLeft(settings.timeLimit);
    setQuizStarted(true);
  };

  const handleAnswerSelection = (value) => {
    setSelectedAnswer(value);
  };

  const handleNextQuestion = () => {
    if (selectedAnswer === quizData[currentQuestion].correctAnswer) {
      setScore(score + 1);
    }

    if (currentQuestion + 1 < quizSettings.questionCount) {
      setCurrentQuestion(currentQuestion + 1);
      setSelectedAnswer('');
    } else {
      setQuizCompleted(true);
    }
  };

  const resetQuiz = () => {
    setQuizStarted(false);
    setQuizSettings(null);
    setCurrentQuestion(0);
    setSelectedAnswer('');
    setScore(0);
    setQuizCompleted(false);
    setTimeLeft(0);
  };

  if (!quizStarted) {
    return <QuizSetup onStartQuiz={startQuiz} />;
  }

  if (quizCompleted) {
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

  const currentQuizQuestion = quizData[currentQuestion];

  return (
    <Card className="w-full max-w-md mx-auto">
      <CardHeader>
        <CardTitle>Question {currentQuestion + 1}</CardTitle>
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

export default QuizApp;