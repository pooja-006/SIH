const skills = ['Python', 'SQL', 'JavaScript', 'React', 'MS Excel', 'Communication', 'AutoCAD', 'Accounting', 'Tally', 'Agriculture', 'Data Analysis', 'Networking', 'Digital Marketing', 'Documentation', 'Field Survey', 'Solar Energy']
export default function SkillSelector({ selected, onChange }) {
  const toggle = (skill) => onChange(selected.includes(skill) ? selected.filter((item) => item !== skill) : [...selected, skill])
  return <div className="grid grid-cols-2 gap-3 sm:grid-cols-4">{skills.map((skill) => <button key={skill} type="button" aria-pressed={selected.includes(skill)} onClick={() => toggle(skill)} className={`chip ${selected.includes(skill) ? 'chip-selected' : ''}`}>{skill}</button>)}</div>
}
