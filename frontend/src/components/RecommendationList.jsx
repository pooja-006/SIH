import InternshipCard from './InternshipCard'
export default function RecommendationList({ recommendations }) { return <div className="space-y-4">{recommendations.slice(0, 5).map((item) => <InternshipCard key={item.internship_id} internship={item} />)}</div> }
