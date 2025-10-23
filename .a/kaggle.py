import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_merge_data(train_path, test_path):
    """train.csv와 test.csv를 읽어 하나의 데이터프레임으로 병합합니다."""
    try:
        train_df = pd.read_csv(train_path)
        test_df = pd.read_csv(test_path)
        return pd.concat([train_df, test_df], ignore_index=True)
    except FileNotFoundError as e:
        print(f'오류: {e}. 파일이 현재 폴더에 있는지 확인하세요.')
        return None

def find_most_correlated(df):
    """'Transported'와 가장 상관관계가 높은 항목을 찾습니다."""
    # 숫자형 데이터의 상관관계를 계산하고 'Transported' 기준 내림차순 정렬
    correlations = df.corr(numeric_only=True)['Transported'].abs().sort_values(ascending=False)
    
    # 첫 번째는 자기 자신이므로(상관계수 1), 두 번째 항목을 반환
    return correlations.index[1], correlations.iloc[1]

def plot_transported_by_age_group(df):
    """나이대별 Transported 여부를 그래프로 시각화합니다."""
    plot_df = df.copy()
    
    # 'Age'의 결측치를 중간값으로 채웁니다.
    plot_df['Age'].fillna(plot_df['Age'].median(), inplace=True)
    
    # 나이 그룹을 생성합니다.
    bins = [0, 10, 20, 30, 40, 50, 60, 70, 100]
    labels = ['10대 미만', '10대', '20대', '30대', '40대', '50대', '60대', '70대 이상']
    plot_df['AgeGroup'] = pd.cut(plot_df['Age'], bins=bins, labels=labels, right=False)

    # 시각화 설정 (한글 폰트 및 스타일)
    plt.figure(figsize=(12, 8))
    plt.rcParams['font.family'] = 'Malgun Gothic'
    sns.set_style('whitegrid')
    
    # 막대 그래프 생성
    sns.countplot(data=plot_df, x='AgeGroup', hue='Transported', palette='viridis')
    
    plt.title('연령대별 Transported 여부', fontsize=16)
    plt.xlabel('연령대', fontsize=12)
    plt.ylabel('승객 수', fontsize=12)
    plt.legend(title='전송 여부')
    plt.show()

if __name__ == '__main__':
    train_file = 'train.csv'
    test_file = 'test.csv'
    
    # 1. 데이터 읽기 및 병합
    full_data = load_and_merge_data(train_file, test_file)
    
    if full_data is not None:
        # 2. 전체 데이터 수량 파악
        print(f'병합된 전체 데이터의 수량: {len(full_data)}개')
        print('-' * 30)

        # 3. 'Transported'와 가장 관련성 높은 항목 찾기 (train 데이터 사용)
        train_data = pd.read_csv(train_file)
        feature, value = find_most_correlated(train_data)
        print(f"'Transported'와 가장 관련성이 높은 항목: '{feature}'")
        print(f"(상관계수 절대값: {value:.4f})")
        print('-' * 30)
        
        # 4. 연령대별 Transported 여부 시각화
        print("연령대별 Transported 여부 그래프를 생성합니다...")
        plot_transported_by_age_group(train_data)
