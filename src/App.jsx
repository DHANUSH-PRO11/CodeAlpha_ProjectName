import { useState, useEffect } from 'react';

const words = ['python', 'hangman', 'developer', 'computer', 'challenge'];
const initialGame = {
  secretWord: '',
  guessedLetters: [],
  incorrectGuesses: 0,
  message: 'Guess a letter to start the game.',
  gameOver: false,
  score: 0,
};

function App() {
  const [game, setGame] = useState(initialGame);
  const [showHangman, setShowHangman] = useState(false);

  useEffect(() => {
    resetGame();
  }, []);

  function resetGame() {
    const word = words[Math.floor(Math.random() * words.length)];
    setGame({
      ...initialGame,
      secretWord: word,
      message: 'Guess a letter to start the game.',
    });
    setShowHangman(false);
  }

  function displayWord() {
    return game.secretWord
      .split('')
      .map((letter) => (game.guessedLetters.includes(letter) ? letter : '_'))
      .join(' ');
  }

  function handleGuess(event) {
    event.preventDefault();
    if (game.gameOver) {
      return;
    }

    const guess = event.target.elements.letter.value.trim().toLowerCase();
    event.target.reset();
    if (!guess || guess.length !== 1 || !guess.match(/^[a-z]$/)) {
      setGame((prev) => ({ ...prev, message: 'Please enter a single valid letter.' }));
      return;
    }
    if (game.guessedLetters.includes(guess)) {
      setGame((prev) => ({ ...prev, message: `You already guessed '${guess}'.` }));
      return;
    }

    const letters = [...game.guessedLetters, guess];
    const correct = game.secretWord.includes(guess);
    const incorrectGuesses = correct ? game.incorrectGuesses : game.incorrectGuesses + 1;
    const wordComplete = game.secretWord.split('').every((ch) => letters.includes(ch));
    const gameOver = incorrectGuesses >= 6 || wordComplete;
    const score = wordComplete ? Math.max(0, 6 - incorrectGuesses) : 0;
    const message = wordComplete
      ? `You won! The word was: ${game.secretWord}. Your score is ${score}.` 
      : gameOver
      ? `You lost! The word was: ${game.secretWord}.`
      : correct
      ? `Good guess: '${guess}' is in the word.`
      : `Wrong guess: '${guess}' is not in the word.`;

    setGame({
      ...game,
      guessedLetters: letters,
      incorrectGuesses,
      message,
      gameOver,
      score,
    });
  }

  return (
    <div className="app-container">
      <header className="brand-bar">
        <div className="header-content">
          <h1>🎮 Hangman Game</h1>
          <p>Guess the word one letter at a time!</p>
        </div>
        <div className="score-badge">
          <span>Score:</span>
          <strong>{game.score}</strong>
        </div>
      </header>

      <main className="game-shell">
        <section className="status-card">
          <div className="status-header">
            <h2>Hangman</h2>
            <div className="remaining-badge">
              <span className={`remaining-number ${game.incorrectGuesses >= 5 ? 'danger' : ''}`}>
                {6 - game.incorrectGuesses}/6
              </span>
            </div>
          </div>
          <div className={`result-message ${game.gameOver ? (game.guessedLetters.length > 0 && game.secretWord.split('').every(ch => game.guessedLetters.includes(ch)) ? 'success' : 'error') : ''}`}>
            {game.message}
          </div>
        </section>

        <section className="game-board">
          <div className="word-section">
            <label className="word-label">Word</label>
            <div className="word-display">{displayWord() || '_ _ _ _'}</div>
          </div>

          <div className="guesses-section">
            <label className="guesses-label">Guesses</label>
            <div className="guesses-row">
              {game.guessedLetters.length ? (
                game.guessedLetters.map((letter) => (
                  <span key={letter} className="letter-badge">{letter}</span>
                ))
              ) : (
                <span className="hint">Letters here</span>
              )}
            </div>
          </div>

          <form className="guess-form" onSubmit={handleGuess}>
            <input 
              name="letter" 
              maxLength="1" 
              placeholder="Letter" 
              disabled={game.gameOver} 
              autoFocus 
              className="letter-input"
            />
            <button type="submit" disabled={game.gameOver} className="guess-button">Guess</button>
            <button type="button" className="restart-button" onClick={resetGame}>New</button>
          </form>
        </section>
      </main>
    </div>
  );
}

export default App;
