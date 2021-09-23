# Paste the below in the Production Sandbox Rails Console

word = "{" 

Slot.all.each do |s|
    if !s.tutors.empty?
        word << "\"#{s.id}\": ["
        s.tutors.each do |t|
            word << "#{t.person_id}, "
        end
        word << "], "
    end
end

word << "}"

puts word
