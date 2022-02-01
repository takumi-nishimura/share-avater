# -----------------------------------------------------------------------
# Author:   Takumi Nishimura (Haptics Lab)
# Created:  2022/02/02
# Summary:  Analysis manager
# -----------------------------------------------------------------------

from MotionAnalysis import MotionAnalysisManager
from QuestionnaireAnalysis import QuestionnaireAnalysisManager

if __name__ in '__main__':
	motionAnalysis = MotionAnalysisManager.MOTIONAN_ALYSIS()
	questionnaireAnalysis = QuestionnaireAnalysisManager.QUESTIONNAIRE_ANALYSIS()

	motionAnalysis.main()

	questionnaireAnalysis.main()

	print('--- finish --- : AnalysisManager')