import pytest
import os
import app

db = app.db
app = app.app

src_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
db_file = os.path.join(src_dir, 'test.db')


@pytest.mark.tryfirst
def pytest_configure(config):
    config.pluginmanager.register(ScorePlugin(), 'score_plugin')


@pytest.fixture
def client():
    if os.path.exists(db_file):
        os.remove(db_file)

    with app.test_client() as client:
        db.create_all()
        yield client


class ScorePlugin:
    TOTAL_SCORE = 4.0

    def __init__(self):
        self.passed = 0
        self.failed = 0

    def pytest_runtest_logreport(self, report):
        if report.when != 'call':
            return

        if report.passed:
            self.passed += 1

        elif report.failed:
            self.failed += 1

    def calc_score(pass_tests, total_tests, max_score):
        if total_tests == 0:
            return 0

        score = (max_score * pass_tests) / (total_tests)
        score = 0.5 * round(score/0.5)
        return score

    def print_score_scale(max_score, total_tests):
        score_list = [
            (ScorePlugin.calc_score(t, total_tests, max_score), t)
            for t in range(0, total_tests + 1)]

        points = score_list[0][0]
        low_limit = upper_limit = score_list[0][1]

        print('Testy\tPunkty')

        for s in score_list[1:]:
            if s[0] == points:
                low_limit = min(low_limit, s[1])
                upper_limit = max(upper_limit, s[1])
                continue

            print(f'{low_limit:02} - {upper_limit:02}\t {points:02} pkt')

            points = s[0]
            low_limit = upper_limit = s[1]

        print(f'{low_limit:02} - {upper_limit:02}\t {points:02} pkt')

    def pytest_sessionfinish(self, session, exitstatus):

        total_tests = self.passed + self.failed
        if total_tests == 0:
            score = prct = 0
        else:
            score = ScorePlugin.calc_score(self.passed,
                                           total_tests,
                                           self.TOTAL_SCORE)

            prct = round(100 * self.passed/(self.passed + self.failed), 1)

        print("\nTwoj wyniki: ")
        print(f"\tNa {total_tests} wykonanych testow {self.passed}"
              f" testow zakonczonych sukcesem ({prct}%).")

        print(f'\tLiczba punktow za zadanie: {score}')
        ScorePlugin.print_score_scale(self.TOTAL_SCORE, total_tests)
