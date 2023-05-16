from domain.Movie import Movie
from domain.Cinema import Cinema
from domain.Schedule import Schedule
from domain.Seat import Seat
from domain.Ticket import Ticket
from repository.MovieRepository import MovieRepository
from repository.CinemaRepository import CinemaRepository
from repository.ScheduleRepository import ScheduleRepository
from repository.SeatRepository import SeatRepository
from repository.TicketRepository import TicketRepository

movieRepository = MovieRepository()
cinemaRepository = CinemaRepository()
scheduleRepository = ScheduleRepository()
seatRepository = SeatRepository()
ticketRepository = TicketRepository()

class TestCase:
    
    @staticmethod
    def createMovies():

        movieRepository.insert(Movie.Builder()\
                                    .name('극장판 짱구는 못말려: 동물소환 닌자 배꼽수비대')\
                                    .description('어느 날 ‘짱구‘와 동갑내기인 5살 ‘진구’를 데리고, 짱구 가족을 찾아온 수상한 여성. 서로의 아이가 바뀌었다는 충격적인 소식을 전한다. 하루아침에 닌자 가문의 후계자 ‘진구’로 불리게 된 짱구는 ‘부리부리 엉덩이 분신술’로 닌자 유치원을 초토화시킨다. 한편, 떡잎마을에 남겨진 진구와 짱구 가족은 짱구를 찾으러 닌자 마을로 향하고, 세상의 중심인 ‘지구의 배꼽’이 흔들리기 시작하며, 지구가 붕괴될 위기에 처하는데… 과연 짱구는 세상을 지켜낼 수 있을까?!')\
                                    .startDate('2023.05.04')\
                                    .nation('일본')\
                                    .director('하시모토 마사카즈')\
                                    .runningTime('100')\
                                    .posterPath('/resource/image/movie1.jpeg')\
                                    .genre('애니메이션')\
                                    .totalSeat('100')\
                                    .build())
        
        movieRepository.insert(Movie.Builder()\
                                    .name('가디언즈 오브 갤럭시: Volume 3')\
                                    .description('‘가모라’를 잃고 슬픔에 빠져 있던 ‘피터 퀼’이 위기에 처한 은하계와 동료를 지키기 위해 다시 한번 가디언즈 팀과 힘을 모으고, 성공하지 못할 경우 그들의 마지막이 될지도 모르는 미션에 나서는 이야기')\
                                    .startDate('2023.05.03')\
                                    .nation('미국')\
                                    .director('제임스 건')\
                                    .runningTime('150')\
                                    .posterPath('/resource/image/movie2.jpeg')\
                                    .genre('액션')\
                                    .totalSeat('100')\
                                    .build())
        
        movieRepository.insert(Movie.Builder()\
                                    .name('드림')\
                                    .description('선수 생활 사상 최악의 위기를 맞은 쏘울리스 축구 선수 홍대(박서준) 계획도, 의지도 없던 홈리스 풋볼 월드컵 감독으로 재능기부에 나서게 된다 각본 없는 각본(?)으로 열정리스 현실파 PD 소민(아이유)이 다큐 제작으로 합류하게 되면서 뜯어진 운동화와 슬리퍼, 늘어진 반팔 티셔츠를 필두로 운동이라고는 한 번도 해본 적 없는 특별한(!) 선수들이 국가대표로 선발된다 택견인지 축구인지 헷갈리는 실력과 발보다 말이 앞서는 홈리스 선수들의 환장할 팀워크, 다큐에 대사와 상황 그리고 진정성 없는 연출을 강요하는 소민에 기가 막히는 감독 홍대 하지만 포기할 틈도 없이, 월드컵 출전일은 코앞으로 다가오는데...! 이들의 도전은 성공할 수 있을까? 쏘울리스 감독, 열정리스 PD, 그리고 홈리스 국대 부족한 것 투성인 드림팀의 생애 단 한 번의 기회!')\
                                    .startDate('2023.04.26')\
                                    .nation('대한민국')\
                                    .director('이병헌')\
                                    .runningTime('125')\
                                    .posterPath('/resource/image/movie3.jpeg')\
                                    .genre('코미디')\
                                    .totalSeat('100')\
                                    .build())
        
        movieRepository.insert(Movie.Builder()\
                                    .name('슈퍼 마리오 브라더스')\
                                    .description('따단-딴-따단-딴 전 세계를 열광시킬 올 타임 슈퍼 어드벤처의 등장! 뉴욕의 평범한 배관공 형제 ‘마리오‘와 ‘루이지’는 배수관 고장으로 위기에 빠진 도시를 구하려다 미스터리한 초록색 파이프 안으로 빨려 들어가게 된다. 파이프를 통해 새로운 세상으로 차원 이동하게 된 형제. 형 ‘마리오‘는 뛰어난 리더십을 지닌 ‘피치‘가 통치하는 버섯왕국에 도착하지만 동생 ‘루이지‘는 빌런 ‘쿠파‘가 있는 다크랜드로 떨어지며 납치를 당하고 ‘마리오’는 동생을 구하기 위해 ‘피치’와 ‘키노피오’의 도움을 받아 ‘쿠파‘에 맞서기로 결심한다. 그러나 슈퍼스타로 세상을 지배하려는 그의 강력한 힘 앞에 이들은 예기치 못한 위험에 빠지게 되는데...! 동생을 구하기 위해! 세상을 지키기 위해! ‘슈퍼 마리오‘로 레벨업 하기 위한 ‘마리오‘의 스펙터클한 스테이지가 시작된다!')\
                                    .startDate('2023.04.26')\
                                    .nation('미국')\
                                    .director('아론 호바스, 마이클 제레닉')\
                                    .runningTime('92')\
                                    .posterPath('/resource/image/movie4.jpeg')\
                                    .genre('애니메이션')\
                                    .totalSeat('100')\
                                    .build())
        
        movieRepository.insert(Movie.Builder()\
                                    .name('존 윅 4')\
                                    .description('죽을 위기에서 살아난 ‘존 윅’은 ‘최고 회의’를 쓰러트릴 방법을 찾아낸다. 비로소 완전한 자유의 희망을 보지만, NEW 빌런 ‘그라몽 후작’과 전 세계의 최강 연합은 ‘존 윅’의 오랜 친구까지 적으로 만들어 버리고, 새로운 위기에 놓인 ‘존 윅’은 최후의 반격을 준비하는데,, 레전드 액션 블록버스터 <존 윅>의 새로운 챕터가 열린다!')\
                                    .startDate('2023.04.12')\
                                    .nation('미국')\
                                    .director('채드 스타헬 스키')\
                                    .runningTime('169')\
                                    .posterPath('/resource/image/movie5.jpeg')\
                                    .genre('액션')\
                                    .totalSeat('100')\
                                    .build())
        
        movieRepository.insert(Movie.Builder()\
                                    .name('스즈메의 문단속')\
                                    .description('“이 근처에 폐허 없니? 문을 찾고 있어” 규슈의 한적한 마을에 살고 있는 소녀 ‘스즈메’는 문을 찾아 여행 중인 청년 ‘소타’를 만난다. 그의 뒤를 쫓아 산속 폐허에서 발견한 낡은 문. ‘스즈메’가 무언가에 이끌리듯 문을 열자 마을에 재난의 위기가 닥쳐오고 가문 대대로 문 너머의 재난을 봉인하는 ‘소타’를 도와 간신히 문을 닫는다. “닫아야만 하잖아요, 여기를!” 재난을 막았다는 안도감도 잠시, 수수께끼의 고양이 ‘다이진’이 나타나 ‘소타’를 의자로 바꿔 버리고 일본 각지의 폐허에 재난을 부르는 문이 열리기 시작하자 ‘스즈메’는 의자가 된 ‘소타’와 함께 재난을 막기 위한 여정에 나선다. “꿈이 아니었어” 규슈, 시코쿠, 고베, 도쿄 재난을 막기 위해 일본 전역을 돌며 필사적으로 문을 닫아가던 중 어릴 적 고향에 닿은 ‘스즈메’는 잊고 있던 진실과 마주하게 되는데…')\
                                    .startDate('2023.03.08')\
                                    .nation('일본')\
                                    .director('신카이 마코토')\
                                    .runningTime('122')\
                                    .posterPath('/resource/image/movie6.jpeg')\
                                    .genre('애니메이션')\
                                    .totalSeat('100')\
                                    .build())
    
    @staticmethod
    def createCinemas():
        cinemaRepository.insert(Cinema.Builder()\
                        .totalSeat('100')\
                        .amount('10000')\
                        .build())

    @staticmethod
    def createSchedules():
        scheduleRepository.insert(Schedule.Builder()\
                                        .movieId('1')\
                                        .cinemaId('1')\
                                        .startTime('10:00')\
                                        .endTime('12:00')\
                                        .remainSeat('100')\
                                        .build())
            
    @staticmethod
    def createSeats():
        for i in range(1, 101):
            seatRepository.insert(Seat.Builder()\
                                    .scheduleId('1')\
                                    .seatNumber(i)\
                                    .reserveYn('N')\
                                    .build())

    @staticmethod
    def createTickets():
        ticketRepository.insert(Ticket.Builder()\
                                        .seatId('1')\
                                        .phoneNumber('01012341234')\
                                        .build())